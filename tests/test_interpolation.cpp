#include <gtest/gtest.h>
#include "LinearInterpolator.hpp"
#include "NewtonInterpolator.hpp"
#include "GslPolynomialInterpolator.hpp"
#include "CardinalCubicSpline.hpp"

// Linear interpolation test
TEST(InterpolatorTest, LinearInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    LinearInterpolator interpolator(x, y);
    
    // We check that the linear interpolation in 1.5 gives the expected value
    EXPECT_NEAR(interpolator(1.5), 2.5, 1e-5);  // Tolerance of 1e-5
}

// Newton's interpolation test
TEST(InterpolatorTest, NewtonInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    NewtonInterpolator interpolator(x, y);
    
    // We check that Newton's interpolation in 1.5 gives the expected value
    EXPECT_NEAR(interpolator(1.5), 2.25, 1e-5);
}

// GSL polynomial interpolation test
TEST(InterpolatorTest, GSLPolynomialInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    GslPolynomialInterpolator interpolator(x, y);
    
    // We check that the polynomial interpolation of GSL in 1.5 gives the expected value
    EXPECT_NEAR(interpolator(1.5), 2.25, 1e-5);
}

// Cubic interpolation test
TEST(InterpolatorTest, CubicSplineInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0, 3.0, 4.0};
    std::vector<double> y = {0.0, 1.0, 4.0, 9.0, 16.0};
    CardinalCubicSpline interpolator(x, y, 0.0, 1.0);
    
    // We check that cubic interpolation at 1.5 gives the expected value
    EXPECT_NEAR(interpolator(1.5), 2.25, 1e-5);
}

// Test for out-of-range values
TEST(InterpolatorTest, OutOfRangeInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    LinearInterpolator interpolator(x, y);
    
    // We expect the out-of-range value to give an error
    EXPECT_THROW(interpolator(3.0), std::out_of_range);
}

// Linear interpolation test with repeated points
TEST(InterpolatorTest, RepeatedXValues) {
    std::vector<double> x = {0.0, 0.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    
    // We expect an error due to repeated values in x
    EXPECT_THROW(LinearInterpolator interpolator(x, y), std::invalid_argument);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
