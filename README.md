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

これらの手順で仮想環境を簡単に管理できます。

情報源
[1] 【手軽に使えるPython仮想環境】Python venvの使い方 | ギークの逆襲 https://www.geeklibrary.jp/counter-attack/python-venv/
[2] venvコマンド(Windows, Mac, Linux) #Python - Qiita https://qiita.com/Koki_Takada/items/6c4ff0035944fdd800d8
[3] Pythonの仮想環境構築 - パッケージ管理編 - Zenn https://zenn.dev/mook_jp/articles/6815e6806b516f
[4] 初めてのPython実践試験学習 第五回「venvでPythonの仮想環境を ... https://www.pythonic-exam.com/archives/8627
[5] Pythonの環境構築をマスターする(pyenv,venv)(WSL2,Ubuntu利用 ... https://zenn.dev/tigrebiz/articles/2822fb4de256d8
[6] 仮想環境: Python環境構築ガイド - python.jp https://www.python.jp/install/windows/venv.html
[7] venv --- 仮想環境の作成 — Python 3.13.2 ドキュメント https://docs.python.org/ja/3.13/library/venv.html
[8] LinuxやmacOSでPythonの仮想環境を構築する方法 - K-Lab https://www.nemotos.net/?p=5469
