"""
Module for generating QR codes with customizable features.

This module provides a function to generate QR codes based on the provided 
data, color, size, border, and version. The generated QR code is returned 
as an image in a memory buffer.

Imports:
    qrcode (qrcode): The qrcode library for generating QR codes.
    Image (PIL.Image): The Python Imaging Library (PIL) for handling images.
    io (io): The io module for working with streams.

Functions:
    genqr(data, color, size, qr_border, qrversion):
        Generates a QR code with the specified parameters and returns it as a 
        memory buffer. If an error occurs, returns an error message.
"""

import qrcode as qr
import io

def genqr(data=None, color="black", size=10, qr_border=5, qrversion=5):
    """
    Generate a QR code with specified customization options.

    Parameters
    ----------
    data : str, optional
        The data to encode in the QR code. If None, returns an error message.
        Default is None.
    color : str, optional
        The color of the QR code. Default is "black".
    size : int, optional
        The size of each box in the QR code, determining the resolution. 
        Default is 10.
    qr_border : int, optional
        The width of the border around the QR code in boxes. Default is 5.
    qrversion : int, optional
        The version of the QR code, which controls the size and data capacity.
        Must be between 1 and 40. Default is 5.

    Returns
    -------
    io.BytesIO or str
        A memory buffer containing the QR code image if successful.
        If an error occurs, returns a string with an error message.
    """
    
    if data is None:
        return "Data cannot be empty."

    # features of qr
    features = qr.QRCode(version=qrversion, box_size=size, border=qr_border)
    features.add_data(data)
    features.make(fit=True)

    # qr image generation
    generate_image = features.make_image(
        fill_color=color, back_color="white")

    # Save to temporary memory buffer
    buffer = io.BytesIO()
    try:
        generate_image.save(buffer, format="PNG")
        buffer.seek(0)
        return buffer
    except Exception as e:
        return f"Something went wrong: {e}"
