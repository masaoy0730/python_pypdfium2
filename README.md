# python_pypdfium2
Pythonでpypdfium2を使う環境の構築を行います。

Pythonで仮想環境を作成し、既存の仮想環境（`myenv`）を利用する手順を以下に説明します。bashを使用している場合の具体的なコマンドも含めています。

### **1. 仮想環境の作成**
既存の仮想環境がない場合は、以下のコマンドで新しい仮想環境を作成します。
```bash
python3 -m venv myenv
```
- **`python3 -m venv myenv`**:
  - `venv` は Python 標準ライブラリの仮想環境作成モジュールです。
  - `myenv` は仮想環境の名前で、任意に変更可能です。
  - このコマンドを実行すると、カレントディレクトリに `myenv` というフォルダが作成されます。

---

### **2. 仮想環境の有効化**
既存の仮想環境（`myenv`）を有効化するには、以下のコマンドを使用します。

```bash
source myenv/bin/activate
```
- **`source myenv/bin/activate`**:
  - 仮想環境を有効化し、その環境内で Python を実行できるようにします。
  - 有効化後、プロンプトが変更され、仮想環境名（例: `(myenv)`）が表示されます。

---

### **3. 仮想環境の無効化**
仮想環境を終了するには以下のコマンドを実行します。

```bash
deactivate
```
- **`deactivate`**:
  - 仮想環境から抜け出し、グローバルな Python 環境に戻ります。

---

### **4. 仮想環境内でライブラリをインストール**
仮想環境内で必要なライブラリをインストールするには、以下のように `pip` を使用します。

```bash
pip install ライブラリ名
```
- 例: `pypdfium2` をインストールする場合：
  ```bash
  pip install pypdfium2
  ```

---

### **5. 仮想環境の確認**
現在利用中の Python が仮想環境内のものか確認するには以下を実行します：

```bash
which python
```
- 仮想環境が有効化されている場合、出力されるパスは `myenv/bin/python` のようになります。

---

### **6. トラブルシューティング**
#### **a. 仮想環境が正しく有効化されない場合**
- 確認ポイント：
  - `myenv/bin/activate` ファイルが存在するか確認してください。
    ```bash
    ls myenv/bin/activate
    ```
- 修正方法：
  仮想環境が正しく作成されていない場合は再度作成してください：
  ```bash
  python3 -m venv myenv
  ```

#### **b. ライブラリが見つからない場合**
- 仮想環境内でライブラリをインストールしていない可能性があります。
- 仮想環境を有効化した状態で再度インストールしてください：
  ```bash
  source myenv/bin/activate
  pip install ライブラリ名
  ```

---

### **まとめ**
1. 新しい仮想環境は `python3 -m venv myenv` コマンドで作成。
2. 仮想環境は `source myenv/bin/activate` コマンドで有効化。
3. 必要なライブラリは仮想環境内で `pip install ライブラリ名` を使用してインストール。
4. 環境から抜けるには `deactivate` コマンドを使用。

pypdfium2を利用できるようにします。
### **1. pypdfium2のインストール**
```
pip install pypdfium2
```
正しくインストールされているか確認。
```
pip show pypdfium2
```
- 出力例：仮想環境
```
Name: pypdfium2
Version: 4.30.1
Summary: Python bindings to PDFium
Home-page: https://github.com/pypdfium2-team/pypdfium2
Author: pypdfium2-team
Author-email: geisserml@gmail.com
License: BSD-3-Clause, Apache-2.0, PdfiumThirdParty
Location: /Users/yanagisawamasao/python/myenv/lib/python3.13/site-packages
```
### **2. pythonの実行**
```
python pdf.py
```
- 出力例
```
Enterprise 㻿earch Engine
導入事例
〒980-0021　宮城県仙台市青葉区中央二丁目9番10号
https://www.toinx.co.jp/
【会社概要】
「I㼀䛷、感動を、䛸䜒䛻。」をスローガン䛻、1954年䛾創業以降、東北䛾I㼀業界䛾リーダー䛸し䛶、東北電力グループを䛿じ䜑䛸する地域䛾お客さ䜎䛾情報シス
テム䛾開発・保守・運用を支え、多く䛾お客さ䜎から䛾信頼や技術力を誇る株式会社トインクス。
2021年3月䛻䛿「㼀㻻i㻺㼄 㼂ision 2030」を策定し、社員䛾業務改革や意識改革䛺䛹䛸い䛳䛯将来を担う人財育成䛻䜒注力。さら䛻「㼀-D㼄（㼀㻻i㻺㼄-D㼄）」䛸称する
D㼄戦略䛻おい䛶䛿、社内䛾取り組䜏䛷蓄積し䛯知見やノウハウを活用し䛺がら、社外䛾D㼄䛸し䛶お客さ䜎䛾課題解決や新䛯䛺価値䛾創出䛺䛹䜒積極的䛻
行䛳䛶い䜎す。
「I㼀䛷、感動を、䛸䜒䛻。」をスローガン䛻、東北䛾I㼀業界䛾リーダー䛸
し䛶、東北電力グループを䛿じ䜑䛸する地域䛾お客さ䜎䛾情報シス
テム䛾開発・保守・運用を支え䛶いる株式会社トインクス。
ファイルサーバ䛾リプレイスをき䛳かけ䛻企
```


