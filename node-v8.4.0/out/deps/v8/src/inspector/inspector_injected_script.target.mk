# This file is generated by gyp; do not edit.

TOOLSET := target
TARGET := inspector_injected_script
### Rules for action "convert_js_to_cpp_char_array":
quiet_cmd__var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array = ACTION _var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array $@
cmd__var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array = LD_LIBRARY_PATH=$(builddir)/lib.host:$(builddir)/lib.target:$$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; cd $(srcdir)/deps/v8/src/inspector; mkdir -p $(obj)/gen/src/inspector; python build/xxd.py InjectedScriptSource_js injected-script-source.js "$(obj)/gen/src/inspector/injected-script-source.h"

$(obj)/gen/src/inspector/injected-script-source.h: obj := $(abs_obj)
$(obj)/gen/src/inspector/injected-script-source.h: builddir := $(abs_builddir)
$(obj)/gen/src/inspector/injected-script-source.h: TOOLSET := $(TOOLSET)
$(obj)/gen/src/inspector/injected-script-source.h: $(srcdir)/deps/v8/src/inspector/build/xxd.py $(srcdir)/deps/v8/src/inspector/injected-script-source.js FORCE_DO_CMD
	$(call do_cmd,_var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array)

all_deps += $(obj)/gen/src/inspector/injected-script-source.h
action__var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array_outputs := $(obj)/gen/src/inspector/injected-script-source.h


### Rules for final target.
# Build our special outputs first.
$(obj).target/deps/v8/src/inspector/inspector_injected_script.stamp: | $(action__var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array_outputs)

# Preserve order dependency of special output on deps.
$(action__var_www_matissewebsite_node_v8_4_0_deps_v8_src_inspector_inspector_gyp_inspector_injected_script_target_convert_js_to_cpp_char_array_outputs): | 

$(obj).target/deps/v8/src/inspector/inspector_injected_script.stamp: TOOLSET := $(TOOLSET)
$(obj).target/deps/v8/src/inspector/inspector_injected_script.stamp:  FORCE_DO_CMD
	$(call do_cmd,touch)

all_deps += $(obj).target/deps/v8/src/inspector/inspector_injected_script.stamp
# Add target alias
.PHONY: inspector_injected_script
inspector_injected_script: $(obj).target/deps/v8/src/inspector/inspector_injected_script.stamp

# Add target alias to "all" target.
.PHONY: all
all: inspector_injected_script

