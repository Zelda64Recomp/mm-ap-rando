# Create a dylib from main.cpp

cmake_minimum_required(VERSION 3.20)

project(RecompMod LANGUAGES C CXX)
set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(RecompMod SHARED ${CMAKE_SOURCE_DIR}/src/main.cpp)

target_include_directories(RecompMod PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/lib/N64ModernRuntime/librecomp/include
)
