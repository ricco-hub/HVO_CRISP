cmd_2153defec1bad0b90768c4818433fbb3744527e6.intermediate := LD_LIBRARY_PATH=/var/www/matissewebsite/node-v8.4.0/out/Release/lib.host:/var/www/matissewebsite/node-v8.4.0/out/Release/lib.target:$$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; cd ../deps/v8/src/inspector; mkdir -p /var/www/matissewebsite/node-v8.4.0/out/Release/obj/gen/src/inspector/protocol /var/www/matissewebsite/node-v8.4.0/out/Release/obj/gen/include/inspector; python ../../third_party/inspector_protocol/CodeGenerator.py --jinja_dir ../../third_party --output_base "/var/www/matissewebsite/node-v8.4.0/out/Release/obj/gen/src/inspector" --config inspector_protocol_config.json
