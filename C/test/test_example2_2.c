#include "unity.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void setUp(void) {}
void tearDown(void) {}

void test_example2_2_should_generate_rc_response_output(void) {
    // 入力ファイル作成
    FILE* in = fopen("rc_input.txt", "w");
    TEST_ASSERT_NOT_NULL(in);
    fputs("5.0, 1000.0, 0.001, 0.0, 0.01, 0.0, 0.001", in);
    fclose(in);

    // 出力ファイル名
    const char* out_file = "rc_output.txt";

    // コマンド実行
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "./bin/example2_2 rc_input.txt %s", out_file);
    int ret = system(cmd);
    TEST_ASSERT_EQUAL_INT(0, ret);

    // 出力ファイル読み込み
    FILE* out = fopen(out_file, "r");
    TEST_ASSERT_NOT_NULL(out);

    char line[256];
    int line_count = 0;
    int has_voltage = 0;

    while (fgets(line, sizeof(line), out)) {
        line_count++;
        if (strstr(line, "5") || strstr(line, "0")) {
            has_voltage = 1;
        }
    }
    fclose(out);

    TEST_ASSERT_GREATER_THAN(0, line_count);
    TEST_ASSERT_TRUE(has_voltage);

    // 後始末
    remove("rc_input.txt");
    remove(out_file);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_example2_2_should_generate_rc_response_output);
    return UNITY_END();
}
