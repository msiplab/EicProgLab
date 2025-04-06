#include "unity.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void setUp(void) {}
void tearDown(void) {}

// 出力バッファから距離値を抽出
double extract_distance(const char* buffer) {
    double d = 0.0;
    const char* marker = strstr(buffer, "近い方の距離:");
    if (marker) {
        sscanf(marker, "近い方の距離: %lf", &d);
    }
    return d;
}

// popenで実行し、標準出力全文を取得
void run_program_with_input(const char* input, char* output_buf, size_t buf_size) {
    FILE* in = fopen("input.txt", "w");
    TEST_ASSERT_NOT_NULL(in);
    fputs(input, in);
    fclose(in);

    FILE* fp = popen("/bin/sh -c \"./bin/practice1_2 < input.txt\"", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char line[256];
    output_buf[0] = '\0';
    while (fgets(line, sizeof(line), fp)) {
        if (strlen(output_buf) + strlen(line) < buf_size - 1) {
            strcat(output_buf, line);
        }
    }

    pclose(fp);
    remove("input.txt");
}

void test_practice1_2_origin(void) {
    char output[4096];
    run_program_with_input("0.0 0.0\n", output, sizeof(output));
    double d = extract_distance(output);
    TEST_ASSERT_DOUBLE_WITHIN(1e-8, 1.41421356, d);
}

void test_practice1_2_positive_far(void) {
    char output[4096];
    run_program_with_input("3.0 3.0\n", output, sizeof(output));
    double d = extract_distance(output);
    TEST_ASSERT_DOUBLE_WITHIN(1e-8, 2.82842712, d);
}

void test_practice1_2_negative_far(void) {
    char output[4096];
    run_program_with_input("-3.0 -3.0\n", output, sizeof(output));
    double d = extract_distance(output);
    TEST_ASSERT_DOUBLE_WITHIN(1e-8, 2.82842712, d);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_practice1_2_origin);
    RUN_TEST(test_practice1_2_positive_far);
    RUN_TEST(test_practice1_2_negative_far);
    return UNITY_END();
}

