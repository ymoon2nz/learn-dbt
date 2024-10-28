{% macro convert_currency(fromPrice, exchangeRate, fromCurrency, toCurrency) %}
    {{fromPrice}} * {{exchangeRate}}
{% endmacro %}