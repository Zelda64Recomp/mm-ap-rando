cmake_minimum_required(VERSION 3.20)

project(MMRecompRandoTest LANGUAGES C CXX)
set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(MMRecompRandoTest ${CMAKE_CURRENT_SOURCE_DIR}/main.cpp)
target_link_libraries(MMRecompRandoTest PRIVATE MMRecompRando)

target_include_directories(MMRecompRandoTest PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/lib/N64ModernRuntime/librecomp/include
)
