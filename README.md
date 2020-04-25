# 概要

- テスト駆動開発（Kent Beck）を頭から Python で書いて行きます
- Python は書けるけど class を定義したりというのはほぼやっていなかったため、その練習も兼ねて。


## 進め方

- commit はチャプターごとに行います
- テストは標準ライブラリの unittest を使います（現時点では。）
  - https://docs.python.org/ja/3/library/unittest.html
- 外部ライブラリも多分使わないので requirements.txt や Pipfile は当面使わない方針でいきます


## ディレクトリ構成

- とりあえずは以下の構成で開始します

```
tdd_python
  ├ src
  │  └money.py
  └ tests
     └ test_money.py
```


## テスト実行


```
$ python -m unittest tests/test_money.py
```

もしくは

```
$ python -m unittest tests.test_money
```

