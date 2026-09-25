# 実験の目的
既存プログラムへの新規機能の追加。

# 課題 1
## 起動方法と終了方法
- nanoなどと同様に、最初の引数のファイルを開くことができる。
- ccでコンパイルした場合、`./a.out <ファイル名>`で起動できる。
- 終了時は `Ctrl + Q` で終了できる。
- `Ctrl + C` や `Ctrl + D` 、 `Ctrl + \` などでは強制終了できない。

## スクリーン移動方法
- 上下左右矢印キーでカーソルを一文字づつ移動することができる。
- `PgUp`、`PgDn` でスクロール(＝ページ単位)での移動ができる。

# 課題 2
| 機能 | 入/出 | エスケープシーケンス | 説明 |
|---|---|---|---|
| カーソルを上へ移動 | 入力 | `ESC[A` | 上矢印キーを押したときに端末から送られる。`editorReadKey()`は`ARROW_UP`に変換する。 |
| カーソルを下へ移動 | 入力 | `ESC[B` | 下矢印キーを押したときに端末から送られる。`ARROW_DOWN`に変換する。 |
| カーソルを右へ移動 | 入力 | `ESC[C` | 右矢印キーを押したときに端末から送られる。`ARROW_RIGHT`に変換する。 |
| カーソルを左へ移動 | 入力 | `ESC[D` | 左矢印キーを押したときに端末から送られる。`ARROW_LEFT`に変換する。 |
| カーソルをホームへ移動 | 入力 | `ESC[H` または `ESCOH` | Homeキーに対応し、`HOME_KEY`に変換する。 |
| カーソルを行末へ移動 | 入力 | `ESC[F` または `ESCOF` | Endキーに対応し、`END_KEY`に変換する。 |
| Deleteキー | 入力 | `ESC[3~` | Deleteキーに対応し、`DEL_KEY`に変換する。 |
| PageUpキー | 入力 | `ESC[5~` | PageUpキーに対応し、`PAGE_UP`に変換する。 |
| PageDownキー | 入力 | `ESC[6~` | PageDownキーに対応し、`PAGE_DOWN`に変換する。 |
| カーソルを右端へ移動 | 出力 | `ESC[999C` | 999列分右へ移動する。端末の列数より十分大きいため、実質的に右端へ移動する。 |
| カーソルを下端へ移動 | 出力 | `ESC[999B` | 999行分下へ移動する。端末の行数より十分大きいため、実質的に下端へ移動する。 |
| カーソル位置の問い合わせ | 出力 | `ESC[6n` | 端末へ現在のカーソル位置を問い合わせる。`getCursorPosition()`で使用する。 |
| カーソル位置の報告 | 入力 | `ESC[n;mR` | 端末が返す応答。nが行番号、mが列番号を表す。 |


# 課題 3
```c
struct editorConfig {
    int cx,cy;  /* Cursor x and y position in characters */
    int rowoff;     /* Offset of row displayed. */
    int coloff;     /* Offset of column displayed. */
    int screenrows; /* Number of rows that we can show */
    int screencols; /* Number of cols that we can show */
    int numrows;    /* Number of rows */
    int rawmode;    /* Is terminal raw mode enabled? */
    erow *row;      /* Rows */
    int dirty;      /* File modified but not saved. */
    char *filename; /* Currently open filename */
    char statusmsg[80];
    time_t statusmsg_time;
};
```

## cx, cy, rowoff, coloff
- `cx`, `cy` は現在表示している画面内でのカーソルの横位置と縦位置を表す。0から始まる値で、端末上の列番号とは1ずれている。
- `rowoff`, `coloff` は画面の最上段に表示しているファイル行の番号と、画面の左端に表示しているファイル上の文字位置を表す。
- `rowoff` はカーソルが画面の最上段や最下段を越えて移動すると、この値を変更して表示範囲を上下へスクロールする。
- `rowoff`が0のとき、画面の最上段にファイルの先頭行が表示されていることを意味する。
- `coloff`は長い行の右側を表示するときに増加し、左側へ戻るときに減少する。
- `coloff`が0のとき、画面の左端にファイルの先頭文字が表示されていることを意味する。
- 実際のファイル上の列位置を求めるときは、`coloff + cx`、行番号を求めるときは、`rowoff + cy`を使う。

**`cx`, `cy`は画面内の相対位置を表し、`rowoff`, `coloff`はファイル内の表示開始位置を表す。**

## screenrows, screencols, numrows, row
- `screenrows`はエディタの本文に利用できる行数で、端末の行数から下2行分を引いた値になる。
- `screencols`はエディタの本文に利用できる列数で、端末の列数と一致する。
- `numrows`は現在開いているファイルの行数で、ファイルを読み込むとき、`editorInsertRow()`が行を1つ追加するたびに増加する。
- `row`はファイルの各行を格納する`erow`構造体の配列へのポインタで、`E.row[i]`がファイルのi行目に対応する。

## rawmode, dirty, filename
- `rawmode`は端末がRawモードになっているかを示す値である。Rawモードでは、入力されたキーをEnterを押すまで待たずに1文字ずつ読み取れる。`enableRawMode()`で1になり、`disableRawMode()`で0になる。
- `dirty`はファイルが変更されたかを表す値である。0なら保存後または未変更、0以外なら変更ありとして扱われる。ステータスバーに`(modified)`を表示したり、未保存状態でCtrl-Qを押したときに警告を出したりするために使われる。
- `filename`は現在開いているファイル名へのポインタである。ステータスバーにファイル名を表示するときや、ファイルを保存するときに使われる。`editorOpen()`で指定された起動引数が設定される。

## statusmsg[80], statusmsg_time
- `statusmsg[80]`は、画面最下行に表示する状態メッセージを格納する文字配列である。警告や操作結果などを表示する。
- `statusmsg_time`は、状態メッセージを設定した時刻である。`editorRefreshScreen()`では、メッセージが設定されてから5秒未満の場合だけ表示する。これにより、古いメッセージがいつまでも画面に残ることを防いでいる。

# 課題 4
8班なので `-`で一行前の先頭へ、`Enter`で一行後の先頭へ移動する機能を追加した。

`-`を押されたら`ARROW_UP`と同様の処理のあと、カーソルの横位置を0にするため、`cx`と`coloff`を0に設定する。

`Enter`も同様に`ARROW_DOWN`の処理後に`cx`, `coloff`を0に設定する。

いかが `git diff`で出力された差分である。

```diff
void editorProcessKeypress(int fd) {
    /* When the file is modified, requires Ctrl-q to be pressed N times
     * before actually quitting. */
    static int quit_times = KILO_QUIT_TIMES;

    int c = editorReadKey(fd);
    switch(c) {
    case CTRL_C:        /* Ctrl-c */
        /* We ignore ctrl-c, it can't be so simple to lose the changes
         * to the edited file. */
        break;
    case CTRL_Q:        /* Ctrl-q */
        /* Quit if the file was already saved. */
        if (E.dirty && quit_times) {
            editorSetStatusMessage("WARNING!!! File has unsaved changes. "
                "Press Ctrl-Q %d more times to quit.", quit_times);
            quit_times--;
            return;
        }
        exit(0);
        break;
    case PAGE_UP:
    case PAGE_DOWN:
        if (c == PAGE_UP && E.cy != 0)
            E.cy = 0;
        else if (c == PAGE_DOWN && E.cy != E.screenrows-1)
            E.cy = E.screenrows-1;
        {
        int times = E.screenrows;
        while(times--)
            editorMoveCursor(c == PAGE_UP ? ARROW_UP:
                                            ARROW_DOWN);
        }
        break;

    case ARROW_UP:
    case ARROW_DOWN:
    case ARROW_LEFT:
    case ARROW_RIGHT:
        editorMoveCursor(c);
        break;
+   case '-':
+       /* Move to the beginning of the previous line. */
+       editorMoveCursor(ARROW_UP);
+       E.cx = 0;
+       E.coloff = 0;
+       break;
+   case ENTER:
+       /* Move to the beginning of the next line. */
+       editorMoveCursor(ARROW_DOWN);
+       E.cx = 0;
+       E.coloff = 0;
+       break;
    case CTRL_L: /* ctrl+l, clear screen */
        /* Just refresht the line as side effect. */
        break;
    case ESC:
        /* Nothing to do for ESC in this mode. */
        break;
    default:
        break;
    }

    quit_times = KILO_QUIT_TIMES; /* Reset it to the original value. */
}
```
