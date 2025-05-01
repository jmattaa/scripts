cmake_minimum_required(VERSION 3.18)
project(__NEWP_PROJNAME__ LANGUAGES C)

file(GLOB_RECURSE SRCS "\${CMAKE_CURRENT_SOURCE_DIR}/src/*.c")
include_directories("\${CMAKE_CURRENT_SOURCE_DIR}/include")

add_executable(\${PROJECT_NAME} \${SRCS})
