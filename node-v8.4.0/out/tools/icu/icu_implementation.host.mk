# This file is generated by gyp; do not edit.

TOOLSET := host
TARGET := icu_implementation
### Rules for final target.
$(obj).host/tools/icu/icu_implementation.stamp: TOOLSET := $(TOOLSET)
$(obj).host/tools/icu/icu_implementation.stamp:  FORCE_DO_CMD
	$(call do_cmd,touch)

all_deps += $(obj).host/tools/icu/icu_implementation.stamp
# Add target alias
.PHONY: icu_implementation
icu_implementation: $(obj).host/tools/icu/icu_implementation.stamp

# Add target alias to "all" target.
.PHONY: all
all: icu_implementation