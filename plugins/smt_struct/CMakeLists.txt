file(GLOB HEADERS "include/steemit/plugins/smt_struct/*.hpp")

add_library( steemit_smt_struct
             ${HEADERS}
             smt_struct_plugin.cpp
             smt_struct_api.cpp
           )

target_link_libraries( steemit_smt_struct steemit_app steemit_chain steemit_protocol )
target_include_directories( steemit_smt_struct
                            PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include" )
