# Test Cases – AdNabuTestStore

---

# 1 – Product Search

## Positive Test Cases

- Verify user can search product using valid product name.
- Verify matching products are displayed for partial keyword search.
- Verify user can search product using uppercase letters.
- Verify search functionality works using lowercase letters.
- Verify search results are displayed when product name contains spaces.

---

## Negative Test Cases

- Verify search does not return irrelevant products for invalid keyword.
- Verify special characters alone do not return unexpected results.
- Verify search field validation when only blank spaces are entered.

---

## Edge Test Cases

- Verify search works correctly with very long product name input.
- Verify search functionality handles rapid multiple searches without breaking.
- Verify search results are displayed correctly when same product exists in multiple variants.
- Verify search works correctly when network speed is slow.

---

# 2 – Add to Cart

## Positive Test Cases

- Verify user can add product to cart successfully.
- Verify cart count is updated after adding product.
- Verify user can add multiple different products to cart.
- Verify added product details are displayed correctly in cart.
- Verify product quantity increases when same product is added multiple times.
- Verify cart retains added products after page refresh.

---

## Negative Test Cases

- Verify system prevents adding out-of-stock product to cart.
- Verify proper error message is displayed when add-to-cart action fails.
- Verify user cannot add unavailable product variants to cart.
- Verify duplicate cart entries are not created unexpectedly.

---

## Edge Test Cases

- Verify maximum allowed product quantity can be added to cart.
- Verify system behavior when user clicks “Add to Cart” multiple times rapidly.
- Verify cart functionality works correctly during poor internet connection.
- Verify cart data persists correctly after browser refresh or reopening browser.