#include "unity.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void setUp(void) {}
void tearDown(void) {}

void test_example1_2_sqrt2(void) {
    const char* input = "2.0\n";
    FILE* in = fopen("input.txt", "w");
    fputs(input, in);
    fclose(in);

    FILE* fp = popen("./bin/example1_2 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[1024] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    // 結果をチェック（近似値に 1.414 が含まれていればOK）
    TEST_ASSERT_NOT_NULL(strstr(buffer, "1.414"));
    TEST_ASSERT_NOT_NULL(strstr(buffer, "の平方根:"));
}

void test_example1_2_sqrt3(void) {
    const char* input = "3.0\n";
    FILE* in = fopen("input.txt", "w");
    fputs(input, in);
    fclose(in);

    FILE* fp = popen("./bin/example1_2 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[1024] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    // 結果をチェック（近似値に 1.414 が含まれていればOK）
    TEST_ASSERT_NOT_NULL(strstr(buffer, "1.732"));
    TEST_ASSERT_NOT_NULL(strstr(buffer, "の平方根:"));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_example1_2_sqrt2);
    RUN_TEST(test_example1_2_sqrt3);
    return UNITY_END();
}
