CC = gcc
CFLAGS = -Iunity -Wall
UNITY_SRC = unity/unity.c
TEST_DIR = test
BIN_DIR = bin
EXAMPLES1_DIR = Examples1

TEST_NAMES = $(patsubst test_%,%,$(basename $(notdir $(wildcard $(TEST_DIR)/test_*.c))))
TEST_BINS = $(TEST_NAMES:%=$(BIN_DIR)/test_%)
CLI_BINS = $(TEST_NAMES:%=$(BIN_DIR)/%)

.PHONY: all test clean $(TEST_NAMES)

all: test

test: $(CLI_BINS) $(TEST_BINS)
	@for bin in $(TEST_BINS); do echo "Running $$bin"; ./$$bin; done

$(TEST_NAMES): %: $(BIN_DIR)/test_% $(BIN_DIR)/%
	@echo "Running $<"
	@./$<

# サポート: make test_example1_1 でもOKにする
test_%: %
	@$(MAKE) $<

$(BIN_DIR)/test_%: $(TEST_DIR)/test_%.c $(UNITY_SRC)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $< $(UNITY_SRC) -o $@

$(BIN_DIR)/%: $(EXAMPLES1_DIR)/%.c
	@mkdir -p $(BIN_DIR)
	$(CC) -o $@ $<

clean:
	rm -rf $(BIN_DIR)




