CC = gcc
CFLAGS = -Iunity -Wall -DUNITY_INCLUDE_DOUBLE
UNITY_SRC = unity/unity.c
TEST_DIR = test
BIN_DIR = bin

# ソースを探すディレクトリ一覧（必要に応じて拡張可）
SRC_DIRS = Examples1 Examples2 Exercises

# テスト名一覧（example1_1, example2_1 など）
TEST_NAMES = $(patsubst test_%,%,$(basename $(notdir $(wildcard $(TEST_DIR)/test_*.c))))

# テスト・CLI バイナリ
TEST_BINS = $(TEST_NAMES:%=$(BIN_DIR)/test_%)
CLI_BINS  = $(foreach name,$(TEST_NAMES),$(BIN_DIR)/$(name))

.PHONY: all test clean $(TEST_NAMES)

all: test

test: $(CLI_BINS) $(TEST_BINS)
	@for bin in $(TEST_BINS); do echo "Running $$bin"; ./$$bin; done

# 個別テスト（例: make example1_1）
$(TEST_NAMES): %: $(BIN_DIR)/test_% $(BIN_DIR)/%
	@echo "Running $<"
	@./$<

# サポート: make test_example1_1
test_%: %
	@$(MAKE) $<

# テストバイナリビルド
$(BIN_DIR)/test_%: $(TEST_DIR)/test_%.c $(UNITY_SRC)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $< $(UNITY_SRC) -o $@ 

# CLIバイナリビルド（Examples1/Examples2 を検索）
define build_cli_template
$(BIN_DIR)/$(1): $$(firstword $$(wildcard $(addsuffix /$(1).c, $(SRC_DIRS))))
	@mkdir -p $$(BIN_DIR)
	$$(CC) -o $$@ $$< -lm
endef

$(foreach name,$(TEST_NAMES),$(eval $(call build_cli_template,$(name))))

clean:
	rm -rf $(BIN_DIR)




