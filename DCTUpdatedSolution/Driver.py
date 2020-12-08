from DCTKarl import DCT_Demo

def main():
    level = int(input("\n\n Input quantization level (integer values from 1 to 100 only):"))
    print("{0} is a {1}".format(level, type(level)))

    dct = DCT_Demo(level)
    print("\n\n Data to be Compressed")
    dct.printMatrix(dct.M,1)
    #Compression
    dct.Calculate_FDCT()
    dct.QuantizationStepForward()
    print("\n\n CompressedMessage")
    dct.printMatrix(dct.C, 1)
    # Decompression
    dct.QuantizationStepInverse()
    dct.Calculate_IDCT()
    print("\n\nDecompressed Message")
    dct.printMatrix(dct.fin,1)
    dct.Compare()


main()