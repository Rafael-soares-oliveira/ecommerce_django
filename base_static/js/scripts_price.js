(function () {
    select_variation = document.getElementById('select-variations');
    variation_price = document.getElementById('variation-price');
    variation_offer_price = document.getElementById('variation-offer-price');

    if (!select_variation) {
        return;
    }

    if (!variation_price) {
        return;
    }

    select_variation.addEventListener('change', function () {
        price = this.options[this.selectedIndex].getAttribute('data-price');
        offer_price = this.options[this.selectedIndex].getAttribute('data-offer-price');

        variation_price.innerHTML = price;

        if (variation_offer_price) {
            variation_offer_price.innerHTML = offer_price;
        }
    })
})();