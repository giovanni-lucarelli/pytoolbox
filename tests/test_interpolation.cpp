#include <gtest/gtest.h>
#include "LinearInterpolator.hpp"
#include "NewtonInterpolator.hpp"
#include "GslPolynomialInterpolator.hpp"
#include "CardinalCubicSpline.hpp"

// Test de interpolación lineal
TEST(InterpolatorTest, LinearInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    LinearInterpolator interpolator(x, y);
    
    // Comprobamos que la interpolación lineal en 1.5 da el valor esperado
    EXPECT_NEAR(interpolator(1.5), 2.5, 1e-5);  // Tolerancia de 1e-5
}
// Test de interpolación de Newton
TEST(InterpolatorTest, NewtonInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    NewtonInterpolator interpolator(x, y);
    
    // Comprobamos que la interpolación de Newton en 1.5 da el valor esperado
    EXPECT_NEAR(interpolator(1.5), 2.5, 1e-5);
}

// Test de interpolación polinómica de GSL
TEST(InterpolatorTest, GSLPolynomialInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    GslPolynomialInterpolator interpolator(x, y);
    
    // Comprobamos que la interpolación polinómica de GSL en 1.5 da el valor esperado
    EXPECT_NEAR(interpolator(1.5), 2.5, 1e-5);
}
// Test de interpolación cúbica
TEST(InterpolatorTest, CubicSplineInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0, 3.0, 4.0};
    std::vector<double> y = {0.0, 1.0, 4.0, 9.0, 16.0};
    CardinalCubicSpline interpolator(x, y, 0.0, 1.0);
    
    // Comprobamos que la interpolación cúbica en 1.5 da el valor esperado
    EXPECT_NEAR(interpolator(1.5), 2.25, 1e-5);
}

// Test de valores fuera del rango (esperamos un error o NaN)
TEST(InterpolatorTest, OutOfRangeInterpolation) {
    std::vector<double> x = {0.0, 1.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    LinearInterpolator interpolator(x, y);
    
    // Esperamos que el valor fuera de rango dé un error o un valor inesperado
    EXPECT_THROW(interpolator(3.0), std::out_of_range);
}
// Test de interpolación con puntos repetidos (posible error)
TEST(InterpolatorTest, RepeatedXValues) {
    std::vector<double> x = {0.0, 0.0, 2.0};
    std::vector<double> y = {0.0, 1.0, 4.0};
    LinearInterpolator interpolator(x, y);
    
    // Esperamos un error debido a valores repetidos en x
    EXPECT_THROW(interpolator(1.0), std::invalid_argument);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
