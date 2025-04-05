#include "unity.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void setUp(void) {}
void tearDown(void) {}

void test_example2_1_norm_should_be_5_for_3_4_vector(void) {
    const char* input = "2\n3\n4\nn\n";  // 入力: 次元=2, 要素3と4, 継続なし

    // 入力ファイル作成
    FILE* in = fopen("input.txt", "w");
    fputs(input, in);
    fclose(in);

    // プログラムを popen で実行
    FILE* fp = popen("./bin/example2_1 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[1024] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    // 出力に "5.000000" を含むことを確認（ノルム）
    TEST_ASSERT_NOT_NULL(strstr(buffer, "5.000000"));
    // 呼び出し回数など他の出力も確認可能（任意）
    TEST_ASSERT_NOT_NULL(strstr(buffer, "getNorm の呼出し回数: 1"));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_example2_1_norm_should_be_5_for_3_4_vector);
    return UNITY_END();
}
