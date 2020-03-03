import diff_match_patch_custom as dmp_module

text1 = ["aa", "bb", "ccd", "dd" ]
text2 = ["aa", "bb", "cc", "bb"]

text1 = ' '.join(text1)
text2 = ' '.join(text2)

print(text1)
print(text2)

dmp = dmp_module.diff_match_patch()

lineText1, lineText2, lineArray = dmp.diff_linesToWords(text1, text2)

diffs = dmp.diff_main(lineText1, lineText2)
dmp.diff_charsToLines(diffs, lineArray)
# dmp.diff_cleanupSemantic(diffs)
print(diffs)
