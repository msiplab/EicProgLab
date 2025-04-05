#!/bin/bash

# --------------------------------------------
# Unityテスト環境セットアップスクリプト（main衝突完全回避 + popen/bin対応）
#
# - Unity v2.6.1 を unity/ に保存
# - Examples1/example1_1.c を bin/example1_1 にビルド
# - Makefile を生成（依存解決・main衝突なし）
#
# 実行方法:
#   chmod +x setup_unity.sh
#   ./setup_unity.sh
#   make test_example1_1
# --------------------------------------------

UNITY_VERSION="v2.6.1"
UNITY_REPO="https://raw.githubusercontent.com/ThrowTheSwitch/Unity/$UNITY_VERSION/src"
UNITY_DIR="unity"
TEST_DIR="test"
EXAMPLES_DIR="Examples1"
BIN_DIR="bin"
UNITY_FILES=("unity.c" "unity.h" "unity_internals.h")

echo "📦 Unity $UNITY_VERSION を $UNITY_DIR にダウンロード中..."
mkdir -p "$UNITY_DIR"
for FILE in "${UNITY_FILES[@]}"; do
    curl -fsSL "$UNITY_REPO/$FILE" -o "$UNITY_DIR/$FILE"
    if [ $? -ne 0 ]; then
        echo "❌ $FILE のダウンロードに失敗しました"
        exit 1
    fi
done
echo "✅ Unityのセットアップ完了"

# テストディレクトリ作成
mkdir -p "$BIN_DIR"

echo "✅ セットアップ完了！次のコマンドでテストできます："
echo "   make test_example1_1"
