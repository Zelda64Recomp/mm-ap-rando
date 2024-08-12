cmake_minimum_required(VERSION 3.20)

project(MMRecompRando LANGUAGES C CXX)
set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(MMRecompRando SHARED ${CMAKE_SOURCE_DIR}/src/main.cpp ${CMAKE_SOURCE_DIR}/src/utils.cpp)

target_include_directories(MMRecompRando PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_SOURCE_DIR}/lib/N64ModernRuntime/librecomp/include
)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
target_include_directories(MMRecompRando PRIVATE ${Python3_INCLUDE_DIRS})
target_link_libraries(MMRecompRando PRIVATE Python3::Python)

# Run python script that packages our mod's zip folder
add_custom_command(TARGET MMRecompRando POST_BUILD
    COMMAND ${Python3_EXECUTABLE} ${CMAKE_SOURCE_DIR}/scripts/package_mod.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Packaging mod zip"
)
