#include "unity.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void setUp(void) {}
void tearDown(void) {}

void test_practice1_1_sin_approximation_1(void) {
    const char* input = "1.0 5\n";  // x = 1.0 (rad), n = 5 (→ 11次まで)

    // 入力ファイルの作成
    FILE* in = fopen("input.txt", "w");
    TEST_ASSERT_NOT_NULL(in);
    fputs(input, in);
    fclose(in);

    // プログラム実行
    FILE* fp = popen("./bin/practice1_1 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[512] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    // 結果チェック（sin(1) ≒ 0.841）
    TEST_ASSERT_NOT_NULL(strstr(buffer, "sin(1"));
    TEST_ASSERT_NOT_NULL(strstr(buffer, "0.84"));  // 近似値が含まれていればOK
}

void test_practice1_1_sin_approximation_2(void) {
    const char* input = "2.0 5\n";  // x = 2.0 (rad), n = 5 (→ 11次まで)

    // 入力ファイルの作成
    FILE* in = fopen("input.txt", "w");
    TEST_ASSERT_NOT_NULL(in);
    fputs(input, in);
    fclose(in);

    // プログラム実行
    FILE* fp = popen("./bin/practice1_1 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[512] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    // 結果チェック（sin(1) ≒ 0.841）
    TEST_ASSERT_NOT_NULL(strstr(buffer, "sin(2"));
    TEST_ASSERT_NOT_NULL(strstr(buffer, "0.90"));  // 近似値が含まれていればOK
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_practice1_1_sin_approximation_1);
    RUN_TEST(test_practice1_1_sin_approximation_2);
    return UNITY_END();
}
