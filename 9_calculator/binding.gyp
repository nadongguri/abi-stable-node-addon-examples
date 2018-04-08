{
  "targets": [
    {
      "target_name": "calculator",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "calculator.cc",
        "<!@(node -p \"require('node-addon-api').bacardi()\")"
      ],
      "dependencies": [
        "<!@(node -p \"require('node-addon-api').gyp\")"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<!@(node -p \"require('node-addon-api').include_bacardi\")",
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}
