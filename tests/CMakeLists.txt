cmake_minimum_required(VERSION 3.10)

find_package(Threads REQUIRED)
find_package(GTest REQUIRED)

include(CTest)
enable_testing()

# Include directories
include_directories(${CMAKE_SOURCE_DIR}/include)

# Crea l'eseguibile per i test
add_executable(DataFrameTests test_dataframe.cpp)
add_executable(InterpolationTests test_interpolation.cpp)

# Link the test executable with core library and GTest
target_link_libraries(DataFrameTests PRIVATE core GTest::GTest GTest::Main Threads::Threads)
target_link_libraries(InterpolationTests PRIVATE interpolation GTest::GTest GTest::Main Threads::Threads)

# Aggiunge il test all'esecuzione dei test
add_test(NAME DataFrameTests COMMAND DataFrameTests)
add_test(NAME InterpolationTests COMMAND InterpolationTests)
