

# FoundationModelLifecycle
<a name="API_FoundationModelLifecycle"></a>

Details about whether a model version is available or deprecated.

## Contents
<a name="API_FoundationModelLifecycle_Contents"></a>

 ** status **   <a name="bedrock-Type-FoundationModelLifecycle-status"></a>
Specifies whether a model version is available (`ACTIVE`) or deprecated (`LEGACY`.  
Type: String  
Valid Values: `ACTIVE | LEGACY`   
Required: Yes

 ** endOfLifeTime **   <a name="bedrock-Type-FoundationModelLifecycle-endOfLifeTime"></a>
Time when model is no longer available for use in all AWS regions  
Type: Timestamp  
Required: No

 ** legacyTime **   <a name="bedrock-Type-FoundationModelLifecycle-legacyTime"></a>
Time when the model enters legacy state  
Type: Timestamp  
Required: No

 ** publicExtendedAccessTime **   <a name="bedrock-Type-FoundationModelLifecycle-publicExtendedAccessTime"></a>
Public extended accesss portion of the legacy period, where users should expect higher pricing  
Type: Timestamp  
Required: No

 ** startOfLifeTime **   <a name="bedrock-Type-FoundationModelLifecycle-startOfLifeTime"></a>
Launch time when the model first becomes available  
Type: Timestamp  
Required: No

## See Also
<a name="API_FoundationModelLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/FoundationModelLifecycle) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/FoundationModelLifecycle) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/FoundationModelLifecycle) 