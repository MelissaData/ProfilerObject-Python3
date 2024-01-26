from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
  lib = ctypes.CDLL('mdProfiler.dll', winmode=0)
elif (os.name == 'nt'):
  lib = ctypes.CDLL('mdProfiler.dll')
else:
  lib = ctypes.CDLL('libmdProfiler.so')

lib.mdProfilerCreate.argtypes = []
lib.mdProfilerCreate.restype = c_void_p
lib.mdProfilerDestroy.argtypes = [c_void_p]
lib.mdProfilerDestroy.restype = None
lib.mdProfilerSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetLicenseString.restype = c_int
lib.mdProfilerSetPathToProfilerDataFiles.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetPathToProfilerDataFiles.restype = None
lib.mdProfilerSetFileName.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetFileName.restype = None
lib.mdProfilerSetAppendMode.argtypes = [c_void_p, c_int]
lib.mdProfilerSetAppendMode.restype = None
lib.mdProfilerSetUserName.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetUserName.restype = None
lib.mdProfilerGetUserName.argtypes = [c_void_p]
lib.mdProfilerGetUserName.restype = c_char_p
lib.mdProfilerSetTableName.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetTableName.restype = None
lib.mdProfilerGetTableName.argtypes = [c_void_p]
lib.mdProfilerGetTableName.restype = c_char_p
lib.mdProfilerSetJobName.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetJobName.restype = None
lib.mdProfilerGetJobName.argtypes = [c_void_p]
lib.mdProfilerGetJobName.restype = c_char_p
lib.mdProfilerSetJobDescription.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetJobDescription.restype = None
lib.mdProfilerGetJobDescription.argtypes = [c_void_p]
lib.mdProfilerGetJobDescription.restype = c_char_p
lib.mdProfilerSetSortAnalysis.argtypes = [c_void_p, c_int]
lib.mdProfilerSetSortAnalysis.restype = None
lib.mdProfilerSetMatchUpAnalysis.argtypes = [c_void_p, c_int]
lib.mdProfilerSetMatchUpAnalysis.restype = None
lib.mdProfilerSetRightFielderAnalysis.argtypes = [c_void_p, c_int]
lib.mdProfilerSetRightFielderAnalysis.restype = None
lib.mdProfilerSetDataAggregation.argtypes = [c_void_p, c_int]
lib.mdProfilerSetDataAggregation.restype = None
lib.mdProfilerInitializeDataFiles.argtypes = [c_void_p]
lib.mdProfilerInitializeDataFiles.restype = c_int
lib.mdProfilerGetInitializeErrorString.argtypes = [c_void_p]
lib.mdProfilerGetInitializeErrorString.restype = c_char_p
lib.mdProfilerGetBuildNumber.argtypes = [c_void_p]
lib.mdProfilerGetBuildNumber.restype = c_char_p
lib.mdProfilerGetDatabaseDate.argtypes = [c_void_p]
lib.mdProfilerGetDatabaseDate.restype = c_char_p
lib.mdProfilerGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdProfilerGetLicenseExpirationDate.restype = c_char_p
lib.mdProfilerGetProfileStartDateTime.argtypes = [c_void_p]
lib.mdProfilerGetProfileStartDateTime.restype = c_char_p
lib.mdProfilerGetProfileEndDateTime.argtypes = [c_void_p]
lib.mdProfilerGetProfileEndDateTime.restype = c_char_p
lib.mdProfilerGetColumnTypeEnum.argtypes = [c_void_p]
lib.mdProfilerGetColumnTypeEnum.restype = c_char_p
lib.mdProfilerGetColumnTypeDescription.argtypes = [c_void_p, c_int]
lib.mdProfilerGetColumnTypeDescription.restype = c_char_p
lib.mdProfilerParseColumnTypeDescription.argtypes = [c_void_p, c_char_p]
lib.mdProfilerParseColumnTypeDescription.restype = c_int
lib.mdProfilerGetDataTypeEnum.argtypes = [c_void_p]
lib.mdProfilerGetDataTypeEnum.restype = c_char_p
lib.mdProfilerGetDataTypeDescription.argtypes = [c_void_p, c_int]
lib.mdProfilerGetDataTypeDescription.restype = c_char_p
lib.mdProfilerParseDataTypeDescription.argtypes = [c_void_p, c_char_p]
lib.mdProfilerParseDataTypeDescription.restype = c_int
lib.mdProfilerGetResultCodeEnum.argtypes = [c_void_p]
lib.mdProfilerGetResultCodeEnum.restype = c_char_p
lib.mdProfilerGetResultCodeDescription.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetResultCodeDescription.restype = c_char_p
lib.mdProfilerAddColumn.argtypes = [c_void_p, c_char_p, c_int, c_int]
lib.mdProfilerAddColumn.restype = None
lib.mdProfilerSetColumnCustomPattern.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdProfilerSetColumnCustomPattern.restype = c_int
lib.mdProfilerSetColumnValueRange.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdProfilerSetColumnValueRange.restype = c_int
lib.mdProfilerSetColumnDefaultValue.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdProfilerSetColumnDefaultValue.restype = c_int
lib.mdProfilerSetColumnSize.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerSetColumnSize.restype = None
lib.mdProfilerSetColumnPrecision.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerSetColumnPrecision.restype = None
lib.mdProfilerSetColumnScale.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerSetColumnScale.restype = None
lib.mdProfilerSetColumnIgnoreOnError.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerSetColumnIgnoreOnError.restype = None
lib.mdProfilerStartProfiling.argtypes = [c_void_p]
lib.mdProfilerStartProfiling.restype = None
lib.mdProfilerSetColumn.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdProfilerSetColumn.restype = None
lib.mdProfilerSetColumnNull.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetColumnNull.restype = None
lib.mdProfilerGetColumnValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnValue.restype = c_char_p
lib.mdProfilerAddRecord.argtypes = [c_void_p]
lib.mdProfilerAddRecord.restype = None
lib.mdProfilerGetResults.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetResults.restype = c_char_p
lib.mdProfilerSetTextQualifier.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetTextQualifier.restype = None
lib.mdProfilerSetColumnDelimiter.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetColumnDelimiter.restype = None
lib.mdProfilerSetRowDelimiter.argtypes = [c_void_p, c_char_p]
lib.mdProfilerSetRowDelimiter.restype = None
lib.mdProfilerAddDelimitedRecord.argtypes = [c_void_p, c_char_p]
lib.mdProfilerAddDelimitedRecord.restype = c_char_p
lib.mdProfilerProfileData.argtypes = [c_void_p]
lib.mdProfilerProfileData.restype = None
lib.mdProfilerGetTableRecordCount.argtypes = [c_void_p]
lib.mdProfilerGetTableRecordCount.restype = c_int
lib.mdProfilerGetTableRecordEmptyCount.argtypes = [c_void_p]
lib.mdProfilerGetTableRecordEmptyCount.restype = c_int
lib.mdProfilerGetTableRecordNullCount.argtypes = [c_void_p]
lib.mdProfilerGetTableRecordNullCount.restype = c_int
lib.mdProfilerGetTableEmbeddedRowDelimiterCount.argtypes = [c_void_p]
lib.mdProfilerGetTableEmbeddedRowDelimiterCount.restype = c_int
lib.mdProfilerGetTableNotAllFieldsPresentCount.argtypes = [c_void_p]
lib.mdProfilerGetTableNotAllFieldsPresentCount.restype = c_int
lib.mdProfilerGetTableExtraFieldsPresentCount.argtypes = [c_void_p]
lib.mdProfilerGetTableExtraFieldsPresentCount.restype = c_int
lib.mdProfilerGetTableUnbalancedTextQualifiersCount.argtypes = [c_void_p]
lib.mdProfilerGetTableUnbalancedTextQualifiersCount.restype = c_int
lib.mdProfilerGetTableUnescapedEmbeddedTextQualifiersCount.argtypes = [c_void_p]
lib.mdProfilerGetTableUnescapedEmbeddedTextQualifiersCount.restype = c_int
lib.mdProfilerGetTableExactMatchDistinctCount.argtypes = [c_void_p]
lib.mdProfilerGetTableExactMatchDistinctCount.restype = c_int
lib.mdProfilerGetTableExactMatchDupesCount.argtypes = [c_void_p]
lib.mdProfilerGetTableExactMatchDupesCount.restype = c_int
lib.mdProfilerGetTableExactMatchLargestGroup.argtypes = [c_void_p]
lib.mdProfilerGetTableExactMatchLargestGroup.restype = c_int
lib.mdProfilerGetTableContactMatchDistinctCount.argtypes = [c_void_p]
lib.mdProfilerGetTableContactMatchDistinctCount.restype = c_int
lib.mdProfilerGetTableContactMatchDupesCount.argtypes = [c_void_p]
lib.mdProfilerGetTableContactMatchDupesCount.restype = c_int
lib.mdProfilerGetTableContactMatchLargestGroup.argtypes = [c_void_p]
lib.mdProfilerGetTableContactMatchLargestGroup.restype = c_int
lib.mdProfilerGetTableHouseholdMatchDistinctCount.argtypes = [c_void_p]
lib.mdProfilerGetTableHouseholdMatchDistinctCount.restype = c_int
lib.mdProfilerGetTableHouseholdMatchDupesCount.argtypes = [c_void_p]
lib.mdProfilerGetTableHouseholdMatchDupesCount.restype = c_int
lib.mdProfilerGetTableHouseholdMatchLargestGroup.argtypes = [c_void_p]
lib.mdProfilerGetTableHouseholdMatchLargestGroup.restype = c_int
lib.mdProfilerGetTableAddressMatchDistinctCount.argtypes = [c_void_p]
lib.mdProfilerGetTableAddressMatchDistinctCount.restype = c_int
lib.mdProfilerGetTableAddressMatchDupesCount.argtypes = [c_void_p]
lib.mdProfilerGetTableAddressMatchDupesCount.restype = c_int
lib.mdProfilerGetTableAddressMatchLargestGroup.argtypes = [c_void_p]
lib.mdProfilerGetTableAddressMatchLargestGroup.restype = c_int
lib.mdProfilerGetColumnCount.argtypes = [c_void_p]
lib.mdProfilerGetColumnCount.restype = c_int
lib.mdProfilerGetColumnName.argtypes = [c_void_p, c_int]
lib.mdProfilerGetColumnName.restype = c_char_p
lib.mdProfilerGetColumnColumnType.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnColumnType.restype = c_int
lib.mdProfilerGetColumnDataType.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDataType.restype = c_int
lib.mdProfilerGetColumnSize.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnSize.restype = c_int
lib.mdProfilerGetColumnPrecision.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnPrecision.restype = c_int
lib.mdProfilerGetColumnScale.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnScale.restype = c_int
lib.mdProfilerGetColumnValueRangeFrom.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnValueRangeFrom.restype = c_char_p
lib.mdProfilerGetColumnValueRangeTo.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnValueRangeTo.restype = c_char_p
lib.mdProfilerGetColumnDefaultValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDefaultValue.restype = c_char_p
lib.mdProfilerGetColumnCustomPatterns.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnCustomPatterns.restype = c_char_p
lib.mdProfilerGetColumnInferredDataType.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnInferredDataType.restype = c_int
lib.mdProfilerGetColumnInferredColumnType.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnInferredColumnType.restype = c_int
lib.mdProfilerGetColumnSortation.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnSortation.restype = c_int
lib.mdProfilerGetColumnSortationPercent.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnSortationPercent.restype = c_double
lib.mdProfilerGetColumnMostPopularCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMostPopularCount.restype = c_int
lib.mdProfilerGetColumnDistinctCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDistinctCount.restype = c_int
lib.mdProfilerGetColumnUniqueCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnUniqueCount.restype = c_int
lib.mdProfilerGetColumnDefaultValueCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDefaultValueCount.restype = c_int
lib.mdProfilerGetColumnBelowRangeCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnBelowRangeCount.restype = c_int
lib.mdProfilerGetColumnAboveRangeCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAboveRangeCount.restype = c_int
lib.mdProfilerGetColumnAboveSizeCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAboveSizeCount.restype = c_int
lib.mdProfilerGetColumnAbovePrecisionCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAbovePrecisionCount.restype = c_int
lib.mdProfilerGetColumnAboveScaleCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAboveScaleCount.restype = c_int
lib.mdProfilerGetColumnInvalidRegExCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnInvalidRegExCount.restype = c_int
lib.mdProfilerGetColumnEmptyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnEmptyCount.restype = c_int
lib.mdProfilerGetColumnNullCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNullCount.restype = c_int
lib.mdProfilerGetColumnInvalidDataCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnInvalidDataCount.restype = c_int
lib.mdProfilerGetColumnInvalidUTF8Count.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnInvalidUTF8Count.restype = c_int
lib.mdProfilerGetColumnNonPrintingCharCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNonPrintingCharCount.restype = c_int
lib.mdProfilerGetColumnDiacriticCharCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDiacriticCharCount.restype = c_int
lib.mdProfilerGetColumnForeignCharCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnForeignCharCount.restype = c_int
lib.mdProfilerGetColumnAlphaOnlyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAlphaOnlyCount.restype = c_int
lib.mdProfilerGetColumnNumericOnlyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericOnlyCount.restype = c_int
lib.mdProfilerGetColumnAlphaNumericCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAlphaNumericCount.restype = c_int
lib.mdProfilerGetColumnUpperCaseOnlyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnUpperCaseOnlyCount.restype = c_int
lib.mdProfilerGetColumnLowerCaseOnlyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnLowerCaseOnlyCount.restype = c_int
lib.mdProfilerGetColumnMixedCaseCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMixedCaseCount.restype = c_int
lib.mdProfilerGetColumnSingleSpaceCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnSingleSpaceCount.restype = c_int
lib.mdProfilerGetColumnMultiSpaceCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMultiSpaceCount.restype = c_int
lib.mdProfilerGetColumnLeadingSpaceCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnLeadingSpaceCount.restype = c_int
lib.mdProfilerGetColumnTrailingSpaceCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTrailingSpaceCount.restype = c_int
lib.mdProfilerGetColumnMaxSpaces.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMaxSpaces.restype = c_int
lib.mdProfilerGetColumnMinSpaces.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMinSpaces.restype = c_int
lib.mdProfilerGetColumnTotalSpaces.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTotalSpaces.restype = c_int
lib.mdProfilerGetColumnTotalWordBreaks.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTotalWordBreaks.restype = c_int
lib.mdProfilerGetColumnAvgSpaces.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAvgSpaces.restype = c_double
lib.mdProfilerGetColumnDecorationCharCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDecorationCharCount.restype = c_int
lib.mdProfilerGetColumnProfanityCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnProfanityCount.restype = c_int
lib.mdProfilerGetColumnInconsistentDataCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnInconsistentDataCount.restype = c_int
lib.mdProfilerGetColumnStringMaxValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringMaxValue.restype = c_char_p
lib.mdProfilerGetColumnStringMinValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringMinValue.restype = c_char_p
lib.mdProfilerGetColumnStringQ1Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringQ1Value.restype = c_char_p
lib.mdProfilerGetColumnStringMedValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringMedValue.restype = c_char_p
lib.mdProfilerGetColumnStringQ3Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringQ3Value.restype = c_char_p
lib.mdProfilerGetColumnStringMaxLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringMaxLength.restype = c_int
lib.mdProfilerGetColumnStringMinLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringMinLength.restype = c_int
lib.mdProfilerGetColumnStringAvgLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringAvgLength.restype = c_double
lib.mdProfilerGetColumnStringQ1Length.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringQ1Length.restype = c_int
lib.mdProfilerGetColumnStringMedLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringMedLength.restype = c_int
lib.mdProfilerGetColumnStringQ3Length.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStringQ3Length.restype = c_int
lib.mdProfilerGetColumnWordMaxValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordMaxValue.restype = c_char_p
lib.mdProfilerGetColumnWordMinValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordMinValue.restype = c_char_p
lib.mdProfilerGetColumnWordQ1Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordQ1Value.restype = c_char_p
lib.mdProfilerGetColumnWordMedValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordMedValue.restype = c_char_p
lib.mdProfilerGetColumnWordQ3Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordQ3Value.restype = c_char_p
lib.mdProfilerGetColumnWordMaxLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordMaxLength.restype = c_int
lib.mdProfilerGetColumnWordMinLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordMinLength.restype = c_int
lib.mdProfilerGetColumnWordAvgLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordAvgLength.restype = c_double
lib.mdProfilerGetColumnWordQ1Length.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordQ1Length.restype = c_int
lib.mdProfilerGetColumnWordMedLength.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordMedLength.restype = c_int
lib.mdProfilerGetColumnWordQ3Length.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnWordQ3Length.restype = c_int
lib.mdProfilerGetColumnMaxWords.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMaxWords.restype = c_int
lib.mdProfilerGetColumnMinWords.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnMinWords.restype = c_int
lib.mdProfilerGetColumnAvgWords.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnAvgWords.restype = c_double
lib.mdProfilerGetColumnNumericMaxValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericMaxValue.restype = c_double
lib.mdProfilerGetColumnNumericMinValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericMinValue.restype = c_double
lib.mdProfilerGetColumnNumericAvgValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericAvgValue.restype = c_double
lib.mdProfilerGetColumnNumericQ1Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericQ1Value.restype = c_double
lib.mdProfilerGetColumnNumericQ1IntValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericQ1IntValue.restype = c_double
lib.mdProfilerGetColumnNumericMedValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericMedValue.restype = c_double
lib.mdProfilerGetColumnNumericMedIntValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericMedIntValue.restype = c_double
lib.mdProfilerGetColumnNumericQ3Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericQ3Value.restype = c_double
lib.mdProfilerGetColumnNumericQ3IntValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericQ3IntValue.restype = c_double
lib.mdProfilerGetColumnNumericStdDevValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNumericStdDevValue.restype = c_double
lib.mdProfilerGetColumnDateMaxValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateMaxValue.restype = c_char_p
lib.mdProfilerGetColumnDateMinValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateMinValue.restype = c_char_p
lib.mdProfilerGetColumnDateAvgValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateAvgValue.restype = c_char_p
lib.mdProfilerGetColumnDateQ1Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateQ1Value.restype = c_char_p
lib.mdProfilerGetColumnDateMedValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateMedValue.restype = c_char_p
lib.mdProfilerGetColumnDateQ3Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateQ3Value.restype = c_char_p
lib.mdProfilerGetColumnTimeMaxValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTimeMaxValue.restype = c_char_p
lib.mdProfilerGetColumnTimeMinValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTimeMinValue.restype = c_char_p
lib.mdProfilerGetColumnTimeAvgValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTimeAvgValue.restype = c_char_p
lib.mdProfilerGetColumnTimeQ1Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTimeQ1Value.restype = c_char_p
lib.mdProfilerGetColumnTimeMedValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTimeMedValue.restype = c_char_p
lib.mdProfilerGetColumnTimeQ3Value.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnTimeQ3Value.restype = c_char_p
lib.mdProfilerGetColumnDateNoCenturyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnDateNoCenturyCount.restype = c_int
lib.mdProfilerGetColumnNameInconsistentOrderCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNameInconsistentOrderCount.restype = c_int
lib.mdProfilerGetColumnNameMultipleNameCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNameMultipleNameCount.restype = c_int
lib.mdProfilerGetColumnNameSuspiciousNameCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnNameSuspiciousNameCount.restype = c_int
lib.mdProfilerGetColumnStateCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStateCount.restype = c_int
lib.mdProfilerGetColumnProvinceCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnProvinceCount.restype = c_int
lib.mdProfilerGetColumnStateProvinceNonStandardCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStateProvinceNonStandardCount.restype = c_int
lib.mdProfilerGetColumnStateProvinceInvalidCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStateProvinceInvalidCount.restype = c_int
lib.mdProfilerGetColumnZipCodeCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnZipCodeCount.restype = c_int
lib.mdProfilerGetColumnPlus4Count.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnPlus4Count.restype = c_int
lib.mdProfilerGetColumnZipCodeInvalidCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnZipCodeInvalidCount.restype = c_int
lib.mdProfilerGetColumnPostalCodeCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnPostalCodeCount.restype = c_int
lib.mdProfilerGetColumnPostalCodeInvalidCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnPostalCodeInvalidCount.restype = c_int
lib.mdProfilerGetColumnZipCodePostalCodeInvalidCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnZipCodePostalCodeInvalidCount.restype = c_int
lib.mdProfilerGetColumnStateZipCodeMismatchCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnStateZipCodeMismatchCount.restype = c_int
lib.mdProfilerGetColumnProvincePostalCodeMismatchCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnProvincePostalCodeMismatchCount.restype = c_int
lib.mdProfilerGetColumnCountryNonStandardCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnCountryNonStandardCount.restype = c_int
lib.mdProfilerGetColumnCountryInvalidCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnCountryInvalidCount.restype = c_int
lib.mdProfilerGetColumnEmailSyntaxCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnEmailSyntaxCount.restype = c_int
lib.mdProfilerGetColumnEmailMobileDomainCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnEmailMobileDomainCount.restype = c_int
lib.mdProfilerGetColumnEmailMisspelledDomainCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnEmailMisspelledDomainCount.restype = c_int
lib.mdProfilerGetColumnEmailSpamtrapDomainCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnEmailSpamtrapDomainCount.restype = c_int
lib.mdProfilerGetColumnEmailDisposableDomainCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnEmailDisposableDomainCount.restype = c_int
lib.mdProfilerGetColumnPhoneInvalidCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetColumnPhoneInvalidCount.restype = c_int
lib.mdProfilerStartDataFrequency.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerStartDataFrequency.restype = c_int
lib.mdProfilerGetDataFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetDataFrequencyValue.restype = c_char_p
lib.mdProfilerGetDataFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetDataFrequencyCount.restype = c_int
lib.mdProfilerGetNextDataFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextDataFrequency.restype = c_int
lib.mdProfilerStartLengthFrequency.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerStartLengthFrequency.restype = c_int
lib.mdProfilerGetLengthFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetLengthFrequencyValue.restype = c_int
lib.mdProfilerGetLengthFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetLengthFrequencyCount.restype = c_int
lib.mdProfilerGetNextLengthFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextLengthFrequency.restype = c_int
lib.mdProfilerStartPatternFrequency.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerStartPatternFrequency.restype = c_int
lib.mdProfilerGetPatternFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetPatternFrequencyValue.restype = c_char_p
lib.mdProfilerGetPatternFrequencyRegEx.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetPatternFrequencyRegEx.restype = c_char_p
lib.mdProfilerGetPatternFrequencyExample.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetPatternFrequencyExample.restype = c_char_p
lib.mdProfilerGetPatternFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetPatternFrequencyCount.restype = c_int
lib.mdProfilerGetNextPatternFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextPatternFrequency.restype = c_int
lib.mdProfilerStartDateFrequency.argtypes = [c_void_p, c_char_p, c_int, c_int]
lib.mdProfilerStartDateFrequency.restype = c_int
lib.mdProfilerGetDateFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetDateFrequencyValue.restype = c_char_p
lib.mdProfilerGetDateFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetDateFrequencyCount.restype = c_int
lib.mdProfilerGetNextDateFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextDateFrequency.restype = c_int
lib.mdProfilerStartSoundExFrequency.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerStartSoundExFrequency.restype = c_int
lib.mdProfilerGetSoundExFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetSoundExFrequencyValue.restype = c_char_p
lib.mdProfilerGetSoundExFrequencyExample.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetSoundExFrequencyExample.restype = c_char_p
lib.mdProfilerGetSoundExFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetSoundExFrequencyCount.restype = c_int
lib.mdProfilerGetNextSoundExFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextSoundExFrequency.restype = c_int
lib.mdProfilerStartWordFrequency.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerStartWordFrequency.restype = c_int
lib.mdProfilerGetWordFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetWordFrequencyValue.restype = c_char_p
lib.mdProfilerGetWordFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetWordFrequencyCount.restype = c_int
lib.mdProfilerGetNextWordFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextWordFrequency.restype = c_int
lib.mdProfilerStartWordLengthFrequency.argtypes = [c_void_p, c_char_p, c_int]
lib.mdProfilerStartWordLengthFrequency.restype = c_int
lib.mdProfilerGetWordLengthFrequencyValue.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetWordLengthFrequencyValue.restype = c_int
lib.mdProfilerGetWordLengthFrequencyCount.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetWordLengthFrequencyCount.restype = c_int
lib.mdProfilerGetNextWordLengthFrequency.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetNextWordLengthFrequency.restype = c_int
lib.mdProfilerSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdProfilerSetReserved.restype = None
lib.mdProfilerGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdProfilerGetReserved.restype = c_char_p

# mdProfiler Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorDatabaseExpired = 2
	ErrorLicenseExpired = 3
	ErrorProfileFile = 4
	ErrorUnknown = 5

class AppendMode(Enum):
	Append = 0
	Report = 1
	Overwrite = 2
	MustNotExist = 3

class ProfilerColumnType(Enum):
	ColumnTypeInt1 = 1
	ColumnTypeInt2 = 2
	ColumnTypeInt4 = 3
	ColumnTypeInt8 = 4
	ColumnTypeUInt1 = 5
	ColumnTypeUInt2 = 6
	ColumnTypeUInt4 = 7
	ColumnTypeUInt8 = 8
	ColumnTypeReal4 = 9
	ColumnTypeReal8 = 10
	ColumnTypeNumeric = 11
	ColumnTypeDecimal = 12
	ColumnTypeCurrency = 13
	ColumnTypeFixedMBCSString = 14
	ColumnTypeVariableMBCSString = 15
	ColumnTypeFixedUnicodeString = 16
	ColumnTypeVariableUnicodeString = 17
	ColumnTypeDate = 18
	ColumnTypeDBDate = 19
	ColumnTypeDBTime = 20
	ColumnTypeDBTime2 = 21
	ColumnTypeDBTimeStamp = 22
	ColumnTypeDBTimeStamp2 = 23
	ColumnTypeDBTimeStampOffset = 24
	ColumnTypeFileTime = 25
	ColumnTypeBoolean = 26
	ColumnTypeGUID = 27
	ColumnTypeBytes = 28
	ColumnTypeImage = 29

class ProfilerDataType(Enum):
	DataTypeFullName = 1
	DataTypeInverseName = 2
	DataTypeNamePrefix = 3
	DataTypeFirstName = 4
	DataTypeMiddleName = 5
	DataTypeLastName = 6
	DataTypeNameSuffix = 7
	DataTypeTitle = 8
	DataTypeCompany = 9
	DataTypeAddress = 10
	DataTypeCity = 11
	DataTypeStateOrProvince = 12
	DataTypeZipOrPostalCode = 13
	DataTypeCityStateZip = 14
	DataTypeCountry = 15
	DataTypePhone = 16
	DataTypeEmail = 17
	DataTypeString = 18
	DataTypeNumeric = 19
	DataTypeDateMDY = 20
	DataTypeDateYMD = 21
	DataTypeDateDMY = 22
	DataTypeBoolean = 23

class Sortation(Enum):
	SortUnknown = 0
	SortStringAscending = 1
	SortStringDescending = 2
	SortNumericAscending = 3
	SortNumericDescending = 4
	SortDateAscending = 5
	SortDateDescending = 6

class Order(Enum):
	OrderNone = 0
	OrderValueAscending = 1
	OrderValueDescending = 2
	OrderCountAscending = 3
	OrderCountDescending = 4

class DateSpan(Enum):
	DateSpanDate = 1
	DateSpanTime = 2
	DateSpanHour = 3
	DateSpanMinute = 4
	DateSpanSecond = 5
	DateSpanMillisecond = 6
	DateSpanDayOfWeek = 7
	DateSpanDay = 8
	DateSpanWeek = 9
	DateSpanMonth = 10
	DateSpanQuarter = 11
	DateSpanYear = 12
	DateSpanDecade = 13
	DateSpanCentury = 14

class mdProfiler(object):
	def __init__(self):
		self.I = lib.mdProfilerCreate()

	def __del__(self):
		lib.mdProfilerDestroy(self.I)

	def SetLicenseString(self, license):
		return lib.mdProfilerSetLicenseString(self.I, license.encode('utf-8'))

	def SetPathToProfilerDataFiles(self, path):
		lib.mdProfilerSetPathToProfilerDataFiles(self.I, path.encode('utf-8'))

	def SetFileName(self, fileName):
		lib.mdProfilerSetFileName(self.I, fileName.encode('utf-8'))

	def SetAppendMode(self, appendMode):
		lib.mdProfilerSetAppendMode(self.I, AppendMode(appendMode).value)

	def SetUserName(self, userName):
		lib.mdProfilerSetUserName(self.I, userName.encode('utf-8'))

	def GetUserName(self):
		return lib.mdProfilerGetUserName(self.I).decode('utf-8')

	def SetTableName(self, tableName):
		lib.mdProfilerSetTableName(self.I, tableName.encode('utf-8'))

	def GetTableName(self):
		return lib.mdProfilerGetTableName(self.I).decode('utf-8')

	def SetJobName(self, jobName):
		lib.mdProfilerSetJobName(self.I, jobName.encode('utf-8'))

	def GetJobName(self):
		return lib.mdProfilerGetJobName(self.I).decode('utf-8')

	def SetJobDescription(self, jobDescription):
		lib.mdProfilerSetJobDescription(self.I, jobDescription.encode('utf-8'))

	def GetJobDescription(self):
		return lib.mdProfilerGetJobDescription(self.I).decode('utf-8')

	def SetSortAnalysis(self, sortAnalysis):
		lib.mdProfilerSetSortAnalysis(self.I, sortAnalysis)

	def SetMatchUpAnalysis(self, matchUpAnalysis):
		lib.mdProfilerSetMatchUpAnalysis(self.I, matchUpAnalysis)

	def SetRightFielderAnalysis(self, rightFielderAnalysis):
		lib.mdProfilerSetRightFielderAnalysis(self.I, rightFielderAnalysis)

	def SetDataAggregation(self, dataAggregation):
		lib.mdProfilerSetDataAggregation(self.I, dataAggregation)

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdProfilerInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdProfilerGetInitializeErrorString(self.I).decode('utf-8')

	def GetBuildNumber(self):
		return lib.mdProfilerGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdProfilerGetDatabaseDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		return lib.mdProfilerGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetProfileStartDateTime(self):
		return lib.mdProfilerGetProfileStartDateTime(self.I).decode('utf-8')

	def GetProfileEndDateTime(self):
		return lib.mdProfilerGetProfileEndDateTime(self.I).decode('utf-8')

	def GetColumnTypeEnum(self):
		return lib.mdProfilerGetColumnTypeEnum(self.I).decode('utf-8')

	def GetColumnTypeDescription(self, columnType):
		return lib.mdProfilerGetColumnTypeDescription(self.I, ProfilerColumnType(columnType).value).decode('utf-8')

	def ParseColumnTypeDescription(self, columnTypeStr):
		return ProfilerColumnType(lib.mdProfilerParseColumnTypeDescription(self.I, columnTypeStr.encode('utf-8')))

	def GetDataTypeEnum(self):
		return lib.mdProfilerGetDataTypeEnum(self.I).decode('utf-8')

	def GetDataTypeDescription(self, dataType):
		return lib.mdProfilerGetDataTypeDescription(self.I, ProfilerDataType(dataType).value).decode('utf-8')

	def ParseDataTypeDescription(self, dataTypeStr):
		return ProfilerDataType(lib.mdProfilerParseDataTypeDescription(self.I, dataTypeStr.encode('utf-8')))

	def GetResultCodeEnum(self):
		return lib.mdProfilerGetResultCodeEnum(self.I).decode('utf-8')

	def GetResultCodeDescription(self, resultStr):
		return lib.mdProfilerGetResultCodeDescription(self.I, resultStr.encode('utf-8')).decode('utf-8')

	def AddColumn(self, columnName, columnType, dataType):
		lib.mdProfilerAddColumn(self.I, columnName.encode('utf-8'), ProfilerColumnType(columnType).value, ProfilerDataType(dataType).value)

	def SetColumnCustomPattern(self, columnName, regEx):
		return lib.mdProfilerSetColumnCustomPattern(self.I, columnName.encode('utf-8'), regEx.encode('utf-8'))

	def SetColumnValueRange(self, columnName, fromStr, toStr):
		return lib.mdProfilerSetColumnValueRange(self.I, columnName.encode('utf-8'), fromStr.encode('utf-8'), toStr.encode('utf-8'))

	def SetColumnDefaultValue(self, columnName, value):
		return lib.mdProfilerSetColumnDefaultValue(self.I, columnName.encode('utf-8'), value.encode('utf-8'))

	def SetColumnSize(self, columnName, size):
		lib.mdProfilerSetColumnSize(self.I, columnName.encode('utf-8'), size)

	def SetColumnPrecision(self, columnName, precision):
		lib.mdProfilerSetColumnPrecision(self.I, columnName.encode('utf-8'), precision)

	def SetColumnScale(self, columnName, scale):
		lib.mdProfilerSetColumnScale(self.I, columnName.encode('utf-8'), scale)

	def SetColumnIgnoreOnError(self, columnName, ignore):
		lib.mdProfilerSetColumnIgnoreOnError(self.I, columnName.encode('utf-8'), ignore)

	def StartProfiling(self):
		lib.mdProfilerStartProfiling(self.I)

	def SetColumn(self, columnName, content):
		lib.mdProfilerSetColumn(self.I, columnName.encode('utf-8'), content.encode('utf-8'))

	def SetColumnNull(self, columnName):
		lib.mdProfilerSetColumnNull(self.I, columnName.encode('utf-8'))

	def GetColumnValue(self, columnName):
		return lib.mdProfilerGetColumnValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def AddRecord(self):
		lib.mdProfilerAddRecord(self.I)

	def GetResults(self, columnName):
		return lib.mdProfilerGetResults(self.I, columnName.encode('utf-8')).decode('utf-8')

	def SetTextQualifier(self, qualifier):
		lib.mdProfilerSetTextQualifier(self.I, qualifier.encode('utf-8'))

	def SetColumnDelimiter(self, delimiter):
		lib.mdProfilerSetColumnDelimiter(self.I, delimiter.encode('utf-8'))

	def SetRowDelimiter(self, delimiter):
		lib.mdProfilerSetRowDelimiter(self.I, delimiter.encode('utf-8'))

	def AddDelimitedRecord(self, record):
		return lib.mdProfilerAddDelimitedRecord(self.I, record.encode('utf-8')).decode('utf-8')

	def ProfileData(self):
		lib.mdProfilerProfileData(self.I)

	def GetTableRecordCount(self):
		return lib.mdProfilerGetTableRecordCount(self.I)

	def GetTableRecordEmptyCount(self):
		return lib.mdProfilerGetTableRecordEmptyCount(self.I)

	def GetTableRecordNullCount(self):
		return lib.mdProfilerGetTableRecordNullCount(self.I)

	def GetTableEmbeddedRowDelimiterCount(self):
		return lib.mdProfilerGetTableEmbeddedRowDelimiterCount(self.I)

	def GetTableNotAllFieldsPresentCount(self):
		return lib.mdProfilerGetTableNotAllFieldsPresentCount(self.I)

	def GetTableExtraFieldsPresentCount(self):
		return lib.mdProfilerGetTableExtraFieldsPresentCount(self.I)

	def GetTableUnbalancedTextQualifiersCount(self):
		return lib.mdProfilerGetTableUnbalancedTextQualifiersCount(self.I)

	def GetTableUnescapedEmbeddedTextQualifiersCount(self):
		return lib.mdProfilerGetTableUnescapedEmbeddedTextQualifiersCount(self.I)

	def GetTableExactMatchDistinctCount(self):
		return lib.mdProfilerGetTableExactMatchDistinctCount(self.I)

	def GetTableExactMatchDupesCount(self):
		return lib.mdProfilerGetTableExactMatchDupesCount(self.I)

	def GetTableExactMatchLargestGroup(self):
		return lib.mdProfilerGetTableExactMatchLargestGroup(self.I)

	def GetTableContactMatchDistinctCount(self):
		return lib.mdProfilerGetTableContactMatchDistinctCount(self.I)

	def GetTableContactMatchDupesCount(self):
		return lib.mdProfilerGetTableContactMatchDupesCount(self.I)

	def GetTableContactMatchLargestGroup(self):
		return lib.mdProfilerGetTableContactMatchLargestGroup(self.I)

	def GetTableHouseholdMatchDistinctCount(self):
		return lib.mdProfilerGetTableHouseholdMatchDistinctCount(self.I)

	def GetTableHouseholdMatchDupesCount(self):
		return lib.mdProfilerGetTableHouseholdMatchDupesCount(self.I)

	def GetTableHouseholdMatchLargestGroup(self):
		return lib.mdProfilerGetTableHouseholdMatchLargestGroup(self.I)

	def GetTableAddressMatchDistinctCount(self):
		return lib.mdProfilerGetTableAddressMatchDistinctCount(self.I)

	def GetTableAddressMatchDupesCount(self):
		return lib.mdProfilerGetTableAddressMatchDupesCount(self.I)

	def GetTableAddressMatchLargestGroup(self):
		return lib.mdProfilerGetTableAddressMatchLargestGroup(self.I)

	def GetColumnCount(self):
		return lib.mdProfilerGetColumnCount(self.I)

	def GetColumnName(self, index):
		return lib.mdProfilerGetColumnName(self.I, index).decode('utf-8')

	def GetColumnColumnType(self, columnName):
		return ProfilerColumnType(lib.mdProfilerGetColumnColumnType(self.I, columnName.encode('utf-8')))

	def GetColumnDataType(self, columnName):
		return ProfilerDataType(lib.mdProfilerGetColumnDataType(self.I, columnName.encode('utf-8')))

	def GetColumnSize(self, columnName):
		return lib.mdProfilerGetColumnSize(self.I, columnName.encode('utf-8'))

	def GetColumnPrecision(self, columnName):
		return lib.mdProfilerGetColumnPrecision(self.I, columnName.encode('utf-8'))

	def GetColumnScale(self, columnName):
		return lib.mdProfilerGetColumnScale(self.I, columnName.encode('utf-8'))

	def GetColumnValueRangeFrom(self, columnName):
		return lib.mdProfilerGetColumnValueRangeFrom(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnValueRangeTo(self, columnName):
		return lib.mdProfilerGetColumnValueRangeTo(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDefaultValue(self, columnName):
		return lib.mdProfilerGetColumnDefaultValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnCustomPatterns(self, columnName):
		return lib.mdProfilerGetColumnCustomPatterns(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnInferredDataType(self, columnName):
		return ProfilerDataType(lib.mdProfilerGetColumnInferredDataType(self.I, columnName.encode('utf-8')))

	def GetColumnInferredColumnType(self, columnName):
		return ProfilerColumnType(lib.mdProfilerGetColumnInferredColumnType(self.I, columnName.encode('utf-8')))

	def GetColumnSortation(self, columnName):
		return Sortation(lib.mdProfilerGetColumnSortation(self.I, columnName.encode('utf-8')))

	def GetColumnSortationPercent(self, columnName):
		return lib.mdProfilerGetColumnSortationPercent(self.I, columnName.encode('utf-8'))

	def GetColumnMostPopularCount(self, columnName):
		return lib.mdProfilerGetColumnMostPopularCount(self.I, columnName.encode('utf-8'))

	def GetColumnDistinctCount(self, columnName):
		return lib.mdProfilerGetColumnDistinctCount(self.I, columnName.encode('utf-8'))

	def GetColumnUniqueCount(self, columnName):
		return lib.mdProfilerGetColumnUniqueCount(self.I, columnName.encode('utf-8'))

	def GetColumnDefaultValueCount(self, columnName):
		return lib.mdProfilerGetColumnDefaultValueCount(self.I, columnName.encode('utf-8'))

	def GetColumnBelowRangeCount(self, columnName):
		return lib.mdProfilerGetColumnBelowRangeCount(self.I, columnName.encode('utf-8'))

	def GetColumnAboveRangeCount(self, columnName):
		return lib.mdProfilerGetColumnAboveRangeCount(self.I, columnName.encode('utf-8'))

	def GetColumnAboveSizeCount(self, columnName):
		return lib.mdProfilerGetColumnAboveSizeCount(self.I, columnName.encode('utf-8'))

	def GetColumnAbovePrecisionCount(self, columnName):
		return lib.mdProfilerGetColumnAbovePrecisionCount(self.I, columnName.encode('utf-8'))

	def GetColumnAboveScaleCount(self, columnName):
		return lib.mdProfilerGetColumnAboveScaleCount(self.I, columnName.encode('utf-8'))

	def GetColumnInvalidRegExCount(self, columnName):
		return lib.mdProfilerGetColumnInvalidRegExCount(self.I, columnName.encode('utf-8'))

	def GetColumnEmptyCount(self, columnName):
		return lib.mdProfilerGetColumnEmptyCount(self.I, columnName.encode('utf-8'))

	def GetColumnNullCount(self, columnName):
		return lib.mdProfilerGetColumnNullCount(self.I, columnName.encode('utf-8'))

	def GetColumnInvalidDataCount(self, columnName):
		return lib.mdProfilerGetColumnInvalidDataCount(self.I, columnName.encode('utf-8'))

	def GetColumnInvalidUTF8Count(self, columnName):
		return lib.mdProfilerGetColumnInvalidUTF8Count(self.I, columnName.encode('utf-8'))

	def GetColumnNonPrintingCharCount(self, columnName):
		return lib.mdProfilerGetColumnNonPrintingCharCount(self.I, columnName.encode('utf-8'))

	def GetColumnDiacriticCharCount(self, columnName):
		return lib.mdProfilerGetColumnDiacriticCharCount(self.I, columnName.encode('utf-8'))

	def GetColumnForeignCharCount(self, columnName):
		return lib.mdProfilerGetColumnForeignCharCount(self.I, columnName.encode('utf-8'))

	def GetColumnAlphaOnlyCount(self, columnName):
		return lib.mdProfilerGetColumnAlphaOnlyCount(self.I, columnName.encode('utf-8'))

	def GetColumnNumericOnlyCount(self, columnName):
		return lib.mdProfilerGetColumnNumericOnlyCount(self.I, columnName.encode('utf-8'))

	def GetColumnAlphaNumericCount(self, columnName):
		return lib.mdProfilerGetColumnAlphaNumericCount(self.I, columnName.encode('utf-8'))

	def GetColumnUpperCaseOnlyCount(self, columnName):
		return lib.mdProfilerGetColumnUpperCaseOnlyCount(self.I, columnName.encode('utf-8'))

	def GetColumnLowerCaseOnlyCount(self, columnName):
		return lib.mdProfilerGetColumnLowerCaseOnlyCount(self.I, columnName.encode('utf-8'))

	def GetColumnMixedCaseCount(self, columnName):
		return lib.mdProfilerGetColumnMixedCaseCount(self.I, columnName.encode('utf-8'))

	def GetColumnSingleSpaceCount(self, columnName):
		return lib.mdProfilerGetColumnSingleSpaceCount(self.I, columnName.encode('utf-8'))

	def GetColumnMultiSpaceCount(self, columnName):
		return lib.mdProfilerGetColumnMultiSpaceCount(self.I, columnName.encode('utf-8'))

	def GetColumnLeadingSpaceCount(self, columnName):
		return lib.mdProfilerGetColumnLeadingSpaceCount(self.I, columnName.encode('utf-8'))

	def GetColumnTrailingSpaceCount(self, columnName):
		return lib.mdProfilerGetColumnTrailingSpaceCount(self.I, columnName.encode('utf-8'))

	def GetColumnMaxSpaces(self, columnName):
		return lib.mdProfilerGetColumnMaxSpaces(self.I, columnName.encode('utf-8'))

	def GetColumnMinSpaces(self, columnName):
		return lib.mdProfilerGetColumnMinSpaces(self.I, columnName.encode('utf-8'))

	def GetColumnTotalSpaces(self, columnName):
		return lib.mdProfilerGetColumnTotalSpaces(self.I, columnName.encode('utf-8'))

	def GetColumnTotalWordBreaks(self, columnName):
		return lib.mdProfilerGetColumnTotalWordBreaks(self.I, columnName.encode('utf-8'))

	def GetColumnAvgSpaces(self, columnName):
		return lib.mdProfilerGetColumnAvgSpaces(self.I, columnName.encode('utf-8'))

	def GetColumnDecorationCharCount(self, columnName):
		return lib.mdProfilerGetColumnDecorationCharCount(self.I, columnName.encode('utf-8'))

	def GetColumnProfanityCount(self, columnName):
		return lib.mdProfilerGetColumnProfanityCount(self.I, columnName.encode('utf-8'))

	def GetColumnInconsistentDataCount(self, columnName):
		return lib.mdProfilerGetColumnInconsistentDataCount(self.I, columnName.encode('utf-8'))

	def GetColumnStringMaxValue(self, columnName):
		return lib.mdProfilerGetColumnStringMaxValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnStringMinValue(self, columnName):
		return lib.mdProfilerGetColumnStringMinValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnStringQ1Value(self, columnName):
		return lib.mdProfilerGetColumnStringQ1Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnStringMedValue(self, columnName):
		return lib.mdProfilerGetColumnStringMedValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnStringQ3Value(self, columnName):
		return lib.mdProfilerGetColumnStringQ3Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnStringMaxLength(self, columnName):
		return lib.mdProfilerGetColumnStringMaxLength(self.I, columnName.encode('utf-8'))

	def GetColumnStringMinLength(self, columnName):
		return lib.mdProfilerGetColumnStringMinLength(self.I, columnName.encode('utf-8'))

	def GetColumnStringAvgLength(self, columnName):
		return lib.mdProfilerGetColumnStringAvgLength(self.I, columnName.encode('utf-8'))

	def GetColumnStringQ1Length(self, columnName):
		return lib.mdProfilerGetColumnStringQ1Length(self.I, columnName.encode('utf-8'))

	def GetColumnStringMedLength(self, columnName):
		return lib.mdProfilerGetColumnStringMedLength(self.I, columnName.encode('utf-8'))

	def GetColumnStringQ3Length(self, columnName):
		return lib.mdProfilerGetColumnStringQ3Length(self.I, columnName.encode('utf-8'))

	def GetColumnWordMaxValue(self, columnName):
		return lib.mdProfilerGetColumnWordMaxValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnWordMinValue(self, columnName):
		return lib.mdProfilerGetColumnWordMinValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnWordQ1Value(self, columnName):
		return lib.mdProfilerGetColumnWordQ1Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnWordMedValue(self, columnName):
		return lib.mdProfilerGetColumnWordMedValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnWordQ3Value(self, columnName):
		return lib.mdProfilerGetColumnWordQ3Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnWordMaxLength(self, columnName):
		return lib.mdProfilerGetColumnWordMaxLength(self.I, columnName.encode('utf-8'))

	def GetColumnWordMinLength(self, columnName):
		return lib.mdProfilerGetColumnWordMinLength(self.I, columnName.encode('utf-8'))

	def GetColumnWordAvgLength(self, columnName):
		return lib.mdProfilerGetColumnWordAvgLength(self.I, columnName.encode('utf-8'))

	def GetColumnWordQ1Length(self, columnName):
		return lib.mdProfilerGetColumnWordQ1Length(self.I, columnName.encode('utf-8'))

	def GetColumnWordMedLength(self, columnName):
		return lib.mdProfilerGetColumnWordMedLength(self.I, columnName.encode('utf-8'))

	def GetColumnWordQ3Length(self, columnName):
		return lib.mdProfilerGetColumnWordQ3Length(self.I, columnName.encode('utf-8'))

	def GetColumnMaxWords(self, columnName):
		return lib.mdProfilerGetColumnMaxWords(self.I, columnName.encode('utf-8'))

	def GetColumnMinWords(self, columnName):
		return lib.mdProfilerGetColumnMinWords(self.I, columnName.encode('utf-8'))

	def GetColumnAvgWords(self, columnName):
		return lib.mdProfilerGetColumnAvgWords(self.I, columnName.encode('utf-8'))

	def GetColumnNumericMaxValue(self, columnName):
		return lib.mdProfilerGetColumnNumericMaxValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericMinValue(self, columnName):
		return lib.mdProfilerGetColumnNumericMinValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericAvgValue(self, columnName):
		return lib.mdProfilerGetColumnNumericAvgValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericQ1Value(self, columnName):
		return lib.mdProfilerGetColumnNumericQ1Value(self.I, columnName.encode('utf-8'))

	def GetColumnNumericQ1IntValue(self, columnName):
		return lib.mdProfilerGetColumnNumericQ1IntValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericMedValue(self, columnName):
		return lib.mdProfilerGetColumnNumericMedValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericMedIntValue(self, columnName):
		return lib.mdProfilerGetColumnNumericMedIntValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericQ3Value(self, columnName):
		return lib.mdProfilerGetColumnNumericQ3Value(self.I, columnName.encode('utf-8'))

	def GetColumnNumericQ3IntValue(self, columnName):
		return lib.mdProfilerGetColumnNumericQ3IntValue(self.I, columnName.encode('utf-8'))

	def GetColumnNumericStdDevValue(self, columnName):
		return lib.mdProfilerGetColumnNumericStdDevValue(self.I, columnName.encode('utf-8'))

	def GetColumnDateMaxValue(self, columnName):
		return lib.mdProfilerGetColumnDateMaxValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDateMinValue(self, columnName):
		return lib.mdProfilerGetColumnDateMinValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDateAvgValue(self, columnName):
		return lib.mdProfilerGetColumnDateAvgValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDateQ1Value(self, columnName):
		return lib.mdProfilerGetColumnDateQ1Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDateMedValue(self, columnName):
		return lib.mdProfilerGetColumnDateMedValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDateQ3Value(self, columnName):
		return lib.mdProfilerGetColumnDateQ3Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnTimeMaxValue(self, columnName):
		return lib.mdProfilerGetColumnTimeMaxValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnTimeMinValue(self, columnName):
		return lib.mdProfilerGetColumnTimeMinValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnTimeAvgValue(self, columnName):
		return lib.mdProfilerGetColumnTimeAvgValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnTimeQ1Value(self, columnName):
		return lib.mdProfilerGetColumnTimeQ1Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnTimeMedValue(self, columnName):
		return lib.mdProfilerGetColumnTimeMedValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnTimeQ3Value(self, columnName):
		return lib.mdProfilerGetColumnTimeQ3Value(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetColumnDateNoCenturyCount(self, columnName):
		return lib.mdProfilerGetColumnDateNoCenturyCount(self.I, columnName.encode('utf-8'))

	def GetColumnNameInconsistentOrderCount(self, columnName):
		return lib.mdProfilerGetColumnNameInconsistentOrderCount(self.I, columnName.encode('utf-8'))

	def GetColumnNameMultipleNameCount(self, columnName):
		return lib.mdProfilerGetColumnNameMultipleNameCount(self.I, columnName.encode('utf-8'))

	def GetColumnNameSuspiciousNameCount(self, columnName):
		return lib.mdProfilerGetColumnNameSuspiciousNameCount(self.I, columnName.encode('utf-8'))

	def GetColumnStateCount(self, columnName):
		return lib.mdProfilerGetColumnStateCount(self.I, columnName.encode('utf-8'))

	def GetColumnProvinceCount(self, columnName):
		return lib.mdProfilerGetColumnProvinceCount(self.I, columnName.encode('utf-8'))

	def GetColumnStateProvinceNonStandardCount(self, columnName):
		return lib.mdProfilerGetColumnStateProvinceNonStandardCount(self.I, columnName.encode('utf-8'))

	def GetColumnStateProvinceInvalidCount(self, columnName):
		return lib.mdProfilerGetColumnStateProvinceInvalidCount(self.I, columnName.encode('utf-8'))

	def GetColumnZipCodeCount(self, columnName):
		return lib.mdProfilerGetColumnZipCodeCount(self.I, columnName.encode('utf-8'))

	def GetColumnPlus4Count(self, columnName):
		return lib.mdProfilerGetColumnPlus4Count(self.I, columnName.encode('utf-8'))

	def GetColumnZipCodeInvalidCount(self, columnName):
		return lib.mdProfilerGetColumnZipCodeInvalidCount(self.I, columnName.encode('utf-8'))

	def GetColumnPostalCodeCount(self, columnName):
		return lib.mdProfilerGetColumnPostalCodeCount(self.I, columnName.encode('utf-8'))

	def GetColumnPostalCodeInvalidCount(self, columnName):
		return lib.mdProfilerGetColumnPostalCodeInvalidCount(self.I, columnName.encode('utf-8'))

	def GetColumnZipCodePostalCodeInvalidCount(self, columnName):
		return lib.mdProfilerGetColumnZipCodePostalCodeInvalidCount(self.I, columnName.encode('utf-8'))

	def GetColumnStateZipCodeMismatchCount(self, columnName):
		return lib.mdProfilerGetColumnStateZipCodeMismatchCount(self.I, columnName.encode('utf-8'))

	def GetColumnProvincePostalCodeMismatchCount(self, columnName):
		return lib.mdProfilerGetColumnProvincePostalCodeMismatchCount(self.I, columnName.encode('utf-8'))

	def GetColumnCountryNonStandardCount(self, columnName):
		return lib.mdProfilerGetColumnCountryNonStandardCount(self.I, columnName.encode('utf-8'))

	def GetColumnCountryInvalidCount(self, columnName):
		return lib.mdProfilerGetColumnCountryInvalidCount(self.I, columnName.encode('utf-8'))

	def GetColumnEmailSyntaxCount(self, columnName):
		return lib.mdProfilerGetColumnEmailSyntaxCount(self.I, columnName.encode('utf-8'))

	def GetColumnEmailMobileDomainCount(self, columnName):
		return lib.mdProfilerGetColumnEmailMobileDomainCount(self.I, columnName.encode('utf-8'))

	def GetColumnEmailMisspelledDomainCount(self, columnName):
		return lib.mdProfilerGetColumnEmailMisspelledDomainCount(self.I, columnName.encode('utf-8'))

	def GetColumnEmailSpamtrapDomainCount(self, columnName):
		return lib.mdProfilerGetColumnEmailSpamtrapDomainCount(self.I, columnName.encode('utf-8'))

	def GetColumnEmailDisposableDomainCount(self, columnName):
		return lib.mdProfilerGetColumnEmailDisposableDomainCount(self.I, columnName.encode('utf-8'))

	def GetColumnPhoneInvalidCount(self, columnName):
		return lib.mdProfilerGetColumnPhoneInvalidCount(self.I, columnName.encode('utf-8'))

	def StartDataFrequency(self, columnName, order):
		return lib.mdProfilerStartDataFrequency(self.I, columnName.encode('utf-8'), Order(order).value)

	def GetDataFrequencyValue(self, columnName):
		return lib.mdProfilerGetDataFrequencyValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetDataFrequencyCount(self, columnName):
		return lib.mdProfilerGetDataFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextDataFrequency(self, columnName):
		return lib.mdProfilerGetNextDataFrequency(self.I, columnName.encode('utf-8'))

	def StartLengthFrequency(self, columnName, order):
		return lib.mdProfilerStartLengthFrequency(self.I, columnName.encode('utf-8'), Order(order).value)

	def GetLengthFrequencyValue(self, columnName):
		return lib.mdProfilerGetLengthFrequencyValue(self.I, columnName.encode('utf-8'))

	def GetLengthFrequencyCount(self, columnName):
		return lib.mdProfilerGetLengthFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextLengthFrequency(self, columnName):
		return lib.mdProfilerGetNextLengthFrequency(self.I, columnName.encode('utf-8'))

	def StartPatternFrequency(self, columnName, order):
		return lib.mdProfilerStartPatternFrequency(self.I, columnName.encode('utf-8'), Order(order).value)

	def GetPatternFrequencyValue(self, columnName):
		return lib.mdProfilerGetPatternFrequencyValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetPatternFrequencyRegEx(self, columnName):
		return lib.mdProfilerGetPatternFrequencyRegEx(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetPatternFrequencyExample(self, columnName):
		return lib.mdProfilerGetPatternFrequencyExample(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetPatternFrequencyCount(self, columnName):
		return lib.mdProfilerGetPatternFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextPatternFrequency(self, columnName):
		return lib.mdProfilerGetNextPatternFrequency(self.I, columnName.encode('utf-8'))

	def StartDateFrequency(self, columnName, order, dateSpan):
		return lib.mdProfilerStartDateFrequency(self.I, columnName.encode('utf-8'), Order(order).value, DateSpan(dateSpan).value)

	def GetDateFrequencyValue(self, columnName):
		return lib.mdProfilerGetDateFrequencyValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetDateFrequencyCount(self, columnName):
		return lib.mdProfilerGetDateFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextDateFrequency(self, columnName):
		return lib.mdProfilerGetNextDateFrequency(self.I, columnName.encode('utf-8'))

	def StartSoundExFrequency(self, columnName, order):
		return lib.mdProfilerStartSoundExFrequency(self.I, columnName.encode('utf-8'), Order(order).value)

	def GetSoundExFrequencyValue(self, columnName):
		return lib.mdProfilerGetSoundExFrequencyValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetSoundExFrequencyExample(self, columnName):
		return lib.mdProfilerGetSoundExFrequencyExample(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetSoundExFrequencyCount(self, columnName):
		return lib.mdProfilerGetSoundExFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextSoundExFrequency(self, columnName):
		return lib.mdProfilerGetNextSoundExFrequency(self.I, columnName.encode('utf-8'))

	def StartWordFrequency(self, columnName, order):
		return lib.mdProfilerStartWordFrequency(self.I, columnName.encode('utf-8'), Order(order).value)

	def GetWordFrequencyValue(self, columnName):
		return lib.mdProfilerGetWordFrequencyValue(self.I, columnName.encode('utf-8')).decode('utf-8')

	def GetWordFrequencyCount(self, columnName):
		return lib.mdProfilerGetWordFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextWordFrequency(self, columnName):
		return lib.mdProfilerGetNextWordFrequency(self.I, columnName.encode('utf-8'))

	def StartWordLengthFrequency(self, columnName, order):
		return lib.mdProfilerStartWordLengthFrequency(self.I, columnName.encode('utf-8'), Order(order).value)

	def GetWordLengthFrequencyValue(self, columnName):
		return lib.mdProfilerGetWordLengthFrequencyValue(self.I, columnName.encode('utf-8'))

	def GetWordLengthFrequencyCount(self, columnName):
		return lib.mdProfilerGetWordLengthFrequencyCount(self.I, columnName.encode('utf-8'))

	def GetNextWordLengthFrequency(self, columnName):
		return lib.mdProfilerGetNextWordLengthFrequency(self.I, columnName.encode('utf-8'))

	def SetReserved(self, key, value):
		lib.mdProfilerSetReserved(self.I, key.encode('utf-8'), value.encode('utf-8'))

	def GetReserved(self, key):
		return lib.mdProfilerGetReserved(self.I, key.encode('utf-8')).decode('utf-8')
