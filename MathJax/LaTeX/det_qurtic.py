# -*- coding: utf-8 -*-

txt = "a[14] a[23] a[32] a[41] - a[13] a[24] a[32] a[41] - a[14] a[22] a[33] a[41] + a[12] a[24] a[33] a[41] + a[13] a[22] a[34] a[41] - a[12] a[23] a[34] a[41] - a[14] a[23] a[31] a[42] + a[13] a[24] a[31] a[42] + a[14] a[21] a[33] a[42] - a[11] a[24] a[33] a[42] - a[13] a[21] a[34] a[42] + a[11] a[23] a[34] a[42] + a[14] a[22] a[31] a[43] - a[12] a[24] a[31] a[43] - a[14] a[21] a[32] a[43] + a[11] a[24] a[32] a[43] + a[12] a[21] a[34] a[43] - a[11] a[22] a[34] a[43] - a[13] a[22] a[31] a[44] + a[12] a[23] a[31] a[44] + a[13] a[21] a[32] a[44] - a[11] a[23] a[32] a[44] - a[12] a[21] a[33] a[44] + a[11] a[22] a[33] a[44]"

txt_replace = txt.replace("[", "_{").replace("]", "}")

print(txt_replace)

"""
a_{14} a_{23} a_{32} a_{41} - a_{13} a_{24} a_{32} a_{41} - a_{14} a_{22} a_{33} a_{41} + a_{12} a_{24} a_{33} a_{41} + a_{13} a_{22} a_{34} a_{41} - a_{12} a_{23} a_{34} a_{41} - a_{14} a_{23} a_{31} a_{42} + a_{13} a_{24} a_{31} a_{42} + a_{14} a_{21} a_{33} a_{42} - a_{11} a_{24} a_{33} a_{42} - a_{13} a_{21} a_{34} a_{42} + a_{11} a_{23} a_{34} a_{42} + a_{14} a_{22} a_{31} a_{43} - a_{12} a_{24} a_{31} a_{43} - a_{14} a_{21} a_{32} a_{43} + a_{11} a_{24} a_{32} a_{43} + a_{12} a_{21} a_{34} a_{43} - a_{11} a_{22} a_{34} a_{43} - a_{13} a_{22} a_{31} a_{44} + a_{12} a_{23} a_{31} a_{44} + a_{13} a_{21} a_{32} a_{44} - a_{11} a_{23} a_{32} a_{44} - a_{12} a_{21} a_{33} a_{44} + a_{11} a_{22} a_{33} a_{44}
"""

