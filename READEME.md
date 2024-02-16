# niwanowa-mangamura

## s3へデプロイ

``` bash
aws s3 sync /mnt/d/dev/mangamura s3://mangamura
```

## kindle整形

1. kindleの対象フォルダに移動
1. .azwファイルたいしてconvazw.pyを実行
    例

    ``` bash
    D:\dev\mangamura\mangamura\src\convazw.py hoge.azw
    ```

1. 実行時に出力されたフォルダを以下に配置

    mangamura
    └[マンガ名]
        └[実行時に指定したフォルダ名]
