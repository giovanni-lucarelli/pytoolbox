#include <gtest/gtest.h>
#include "DataFrame.hpp"


TEST(DataFrameTest, AddColumn) {
    DataFrame df;
    ColumnType column = {1.0, 2.0, 3.0};
    df.add_column("Col1", column);
    EXPECT_EQ(df.shape(), std::make_pair(3u, 1u));
    EXPECT_EQ(df.get_header().size(), 1u);
    EXPECT_EQ(df.get_header()[0], "Col1");
}


TEST(DataFrameTest, GetColumn) {
    DataFrame df;
    ColumnType column = {1.0, 2.0, 3.0};
    df.add_column("Col1", column);
    const auto& retrieved_column = df.get_column(0);
    EXPECT_EQ(retrieved_column.size(), 3u);
    EXPECT_EQ(std::get<double>(*retrieved_column[0]), 1.0);
}


TEST(DataFrameTest, MeanCalculation) {
    DataFrame df;
    ColumnType column = {1.0, 2.0, 3.0};
    df.add_column("Col1", column);
    EXPECT_DOUBLE_EQ(df.mean("Col1"), 2.0);
}


TEST(DataFrameTest, MinMaxCalculation) {
    DataFrame df;
    ColumnType column = {1.0, 2.0, 3.0};
    df.add_column("Col1", column);
    EXPECT_DOUBLE_EQ(df.min("Col1"), 1.0);
    EXPECT_DOUBLE_EQ(df.max("Col1"), 3.0);
}


TEST(DataFrameTest, StandardDeviation) {
    DataFrame df;
    ColumnType column = {2.0, 4.0, 6.0};
    df.add_column("Col1", column);
    EXPECT_DOUBLE_EQ(df.sd("Col1"), 2.0);
}


TEST(DataFrameTest, DropRow) {
    DataFrame df;
    ColumnType column = {1.0, 2.0, 3.0};
    df.add_column("Col1", column);
    df.drop_row(1);
    EXPECT_EQ(df.shape(), std::make_pair(2u, 1u));
    const auto& retrieved_column = df.get_column(0);
    EXPECT_EQ(std::get<double>(*retrieved_column[1]), 3.0);
}


TEST(DataFrameTest, DropColumn) {
    DataFrame df;
    ColumnType column1 = {1.0, 2.0, 3.0};
    ColumnType column2 = {"A", "B", "C"};
    df.add_column("Col1", column1);
    df.add_column("Col2", column2);
    df.drop_col("Col1");
    EXPECT_EQ(df.shape(), std::make_pair(3u, 1u));
    EXPECT_EQ(df.get_header()[0], "Col2");
}

TEST(DataFrameTest, DropRowWithNaN) {
    DataFrame df;
    ColumnType column = {1.0, std::nullopt, 3.0};
    df.add_column("Col1", column);
    df.drop_row_nan();
    EXPECT_EQ(df.shape(), std::make_pair(2u, 1u));
    const auto& retrieved_column = df.get_column(0);
    EXPECT_EQ(std::get<double>(*retrieved_column[0]), 1.0);
    EXPECT_EQ(std::get<double>(*retrieved_column[1]), 3.0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    ::testing::TestEventListeners& listeners = ::testing::UnitTest::GetInstance()->listeners();
    listeners.Append(new ::testing::EmptyTestEventListener());
    return RUN_ALL_TESTS();
}

