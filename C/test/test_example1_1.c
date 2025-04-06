#include "unity.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void setUp(void) {}
void tearDown(void) {}

void test_example1_1_positive1(void) {
    const char* input = "1.0 10\n";
    FILE* in = fopen("input.txt", "w");
    fputs(input, in);
    fclose(in);

    FILE* fp = popen("./bin/example1_1 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[512] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    TEST_ASSERT_NOT_NULL(strstr(buffer, "e^(1)"));
    TEST_ASSERT_NOT_NULL(strstr(buffer, "2.718"));
}

void test_example1_1_negative1(void) {
    const char* input = "-1.0 10\n";
    FILE* in = fopen("input.txt", "w");
    fputs(input, in);
    fclose(in);

    FILE* fp = popen("./bin/example1_1 < input.txt", "r");
    TEST_ASSERT_NOT_NULL(fp);

    char buffer[512] = {0};
    fread(buffer, 1, sizeof(buffer) - 1, fp);
    pclose(fp);
    remove("input.txt");

    TEST_ASSERT_NOT_NULL(strstr(buffer, "e^(-1)"));
    TEST_ASSERT_NOT_NULL(strstr(buffer, "0.367"));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_example1_1_positive1);
    RUN_TEST(test_example1_1_negative1);
    return UNITY_END();
}
