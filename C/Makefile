CC = gcc
CFLAGS = -Iunity -Wall
UNITY_SRC = unity/unity.c
TEST_DIR = test
BIN_DIR = bin
EXAMPLES_DIR = Examples1

TESTS = $(basename $(notdir $(wildcard $(TEST_DIR)/test_*.c)))
TEST_BINS = $(TESTS:%=$(BIN_DIR)/%)
CLI_BINS = $(BIN_DIR)/example1_1

.PHONY: all test clean $(TESTS)

all: test

test: $(CLI_BINS) $(TEST_BINS)
	@for bin in $(TEST_BINS); do echo "Running $$bin"; ./$$bin; done

# 個別テスト実行（依存するCLIバイナリも先にビルド）
$(TESTS): %: $(BIN_DIR)/% $(CLI_BINS)
	@echo "Running $<"
	@./$<

# テストビルド（example1_1.c はリンクしない）
$(BIN_DIR)/%: $(TEST_DIR)/%.c $(UNITY_SRC)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $< $(UNITY_SRC) -o $@

# CLI バイナリは bin/ 以下にビルド
$(BIN_DIR)/example1_1: $(EXAMPLES_DIR)/example1_1.c
	@mkdir -p $(BIN_DIR)
	$(CC) -o $@ $<

clean:
	rm -rf $(BIN_DIR)