{
  "targets": [
    {
      "target_name": "calculator",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [ "gen/bacardi.cc", "gen/calculator_bridge.cc", "calculator.cc" ],
      "dependencies": [
        "<!@(node -p \"require('node-addon-api').gyp\")",
        "<!@(node -p \"require('node-addon-api').gyp_bacardi\")",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<!@(node -p \"require('node-addon-api').include_bacardi\")",
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}
