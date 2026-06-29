

# SensitiveDataConfiguration
<a name="API_data-automation_SensitiveDataConfiguration"></a>

Configuration for detecting and redacting sensitive data in content. Use this to control whether sensitive data is detected only or both detected and redacted, specify the scope of detection (standard output, custom output, or both), and configure specific PII entity types to detect along with how they should be masked when redacted.

## Contents
<a name="API_data-automation_SensitiveDataConfiguration_Contents"></a>

 ** detectionMode **   <a name="bedrock-Type-data-automation_SensitiveDataConfiguration-detectionMode"></a>
Specifies the mode for handling sensitive data detection. Set to DETECTION to only identify sensitive data without modifying content - this produces one output file per detection scope containing detection information with original unredacted content. Set to DETECTION\_AND\_REDACTION to both identify and mask sensitive data - this produces two output files per detection scope: one unredacted file with detection information and one redacted file with masking applied to sensitive content. For example, if detectionScope includes both STANDARD and CUSTOM with DETECTION\_AND\_REDACTION mode, four output files will be generated (two for standard output and two for custom output).  
Type: String  
Valid Values: `DETECTION | DETECTION_AND_REDACTION`   
Required: Yes

 ** detectionScope **   <a name="bedrock-Type-data-automation_SensitiveDataConfiguration-detectionScope"></a>
Defines which BDA output types to apply sensitive data detection to. Specify STANDARD to detect sensitive data in standard output, CUSTOM to detect in custom output (blueprint-based extraction), or both to apply detection to both output types. If not specified, defaults to both STANDARD and CUSTOM. The number of output files generated depends on both the detection mode and the scopes selected - each scope specified will produce its own set of output files according to the detection mode configured.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Valid Values: `STANDARD | CUSTOM`   
Required: No

 ** piiEntitiesConfiguration **   <a name="bedrock-Type-data-automation_SensitiveDataConfiguration-piiEntitiesConfiguration"></a>
Configuration for detecting and redacting Personally Identifiable Information (PII) entities.   
Type: [PIIEntitiesConfiguration](API_data-automation_PIIEntitiesConfiguration.md) object  
Required: No

## See Also
<a name="API_data-automation_SensitiveDataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/SensitiveDataConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/SensitiveDataConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/SensitiveDataConfiguration) 