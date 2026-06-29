

# DataAutomationLibrarySummary
<a name="API_data-automation_DataAutomationLibrarySummary"></a>

A summary of a data automation library.

## Contents
<a name="API_data-automation_DataAutomationLibrarySummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-data-automation_DataAutomationLibrarySummary-creationTime"></a>
When the library was created.  
Type: Timestamp  
Required: Yes

 ** libraryArn **   <a name="bedrock-Type-data-automation_DataAutomationLibrarySummary-libraryArn"></a>
The library's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** libraryName **   <a name="bedrock-Type-data-automation_DataAutomationLibrarySummary-libraryName"></a>
The library's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: No

## See Also
<a name="API_data-automation_DataAutomationLibrarySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DataAutomationLibrarySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DataAutomationLibrarySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DataAutomationLibrarySummary) 