import pandas as pd
import js
from decimal import Decimal, ROUND_HALF_UP

# Track last modified input
last_modified = None

def get_input_value(element_id):
    """Get value from HTML input element using Pyodide's js module"""
    element = js.document.getElementById(element_id)
    if element and element.value:
        try:
            # Use Decimal for precise floating point arithmetic
            return Decimal(str(element.value))
        except:
            return None
    return None

def set_input_value(element_id, value):
    """Set value to HTML input element"""
    element = js.document.getElementById(element_id)
    if element:
        # Format to 2 decimal places with proper rounding
        if isinstance(value, Decimal):
            formatted_value = float(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        else:
            formatted_value = float(value)
        element.value = f"{formatted_value:.2f}"

def set_text_content(element_id, text):
    """Set text content of HTML element"""
    element = js.document.getElementById(element_id)
    if element:
        element.textContent = text

def toggle_element_visibility(element_id, show):
    """Toggle visibility of HTML element"""
    element = js.document.getElementById(element_id)
    if element:
        if show:
            element.classList.remove('hidden')
        else:
            element.classList.add('hidden')

def convert_temperature(celsius_val, fahrenheit_val, last_modified_input):
    """
    Convert temperature using Pandas DataFrame for data handling.
    Uses Decimal for precise financial-grade floating point calculations.
    """
    # Create DataFrame to store temperature data
    temp_data = {
        'celsius': [float(celsius_val) if celsius_val is not None else None],
        'fahrenheit': [float(fahrenheit_val) if fahrenheit_val is not None else None],
        'source_type': [None],
        'converted_value': [None]
    }
    df = pd.DataFrame(temp_data)
    
    source_value = None
    source_type = None
    
    # Determine source value based on last modified input
    if last_modified_input == 'celsius' and celsius_val is not None:
        source_value = celsius_val
        source_type = 'celsius'
    elif last_modified_input == 'fahrenheit' and fahrenheit_val is not None:
        source_value = fahrenheit_val
        source_type = 'fahrenheit'
    elif celsius_val is not None and fahrenheit_val is not None:
        # Both have values, use the last modified one
        if last_modified_input == 'fahrenheit':
            source_value = fahrenheit_val
            source_type = 'fahrenheit'
        else:
            source_value = celsius_val
            source_type = 'celsius'
    elif celsius_val is not None:
        source_value = celsius_val
        source_type = 'celsius'
    elif fahrenheit_val is not None:
        source_value = fahrenheit_val
        source_type = 'fahrenheit'
    
    if source_value is None:
        return {'success': False, 'message': 'Please enter a temperature value in either Celsius or Fahrenheit.'}
    
    # Perform conversion with precise decimal arithmetic
    if source_type == 'celsius':
        # C to F: F = C * 9/5 + 32
        # Use Decimal for precise calculation
        converted = (source_value * Decimal('9') / Decimal('5')) + Decimal('32')
        target_id = 'fahrenheit-input'
        result_text = f"{float(source_value)}°C = {float(converted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)):.2f}°F"
        new_last_modified = 'celsius'
    else:
        # F to C: C = (F - 32) * 5/9
        converted = (source_value - Decimal('32')) * Decimal('5') / Decimal('9')
        target_id = 'celsius-input'
        result_text = f"{float(source_value)}°F = {float(converted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)):.2f}°C"
        new_last_modified = 'fahrenheit'
    
    # Update DataFrame with results
    df.at[0, 'source_type'] = source_type
    df.at[0, 'converted_value'] = float(converted)
    
    return {
        'success': True,
        'target_id': target_id,
        'converted_value': converted,
        'result_text': result_text,
        'last_modified': new_last_modified
    }
