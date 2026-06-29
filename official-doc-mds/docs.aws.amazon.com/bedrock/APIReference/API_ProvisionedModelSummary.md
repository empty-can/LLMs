

# ProvisionedModelSummary
<a name="API_ProvisionedModelSummary"></a>

A summary of information about a Provisioned Throughput.

This data type is used in the following API operations:
+  [ListProvisionedThroughputs response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListProvisionedModelThroughputs.html#API_ListProvisionedModelThroughputs_ResponseSyntax) 

## Contents
<a name="API_ProvisionedModelSummary_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-ProvisionedModelSummary-creationTime"></a>
The time that the Provisioned Throughput was created.   
Type: Timestamp  
Required: Yes

 ** desiredModelArn **   <a name="bedrock-Type-ProvisionedModelSummary-desiredModelArn"></a>
The Amazon Resource Name (ARN) of the model requested to be associated to this Provisioned Throughput. This value differs from the `modelArn` if updating hasn't completed.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** desiredModelUnits **   <a name="bedrock-Type-ProvisionedModelSummary-desiredModelUnits"></a>
The number of model units that was requested to be allocated to the Provisioned Throughput.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: Yes

 ** foundationModelArn **   <a name="bedrock-Type-ProvisionedModelSummary-foundationModelArn"></a>
The Amazon Resource Name (ARN) of the base model for which the Provisioned Throughput was created, or of the base model that the custom model for which the Provisioned Throughput was created was customized.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}`   
Required: Yes

 ** lastModifiedTime **   <a name="bedrock-Type-ProvisionedModelSummary-lastModifiedTime"></a>
The time that the Provisioned Throughput was last modified.   
Type: Timestamp  
Required: Yes

 ** modelArn **   <a name="bedrock-Type-ProvisionedModelSummary-modelArn"></a>
The Amazon Resource Name (ARN) of the model associated with the Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/((imported)|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}))(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}))`   
Required: Yes

 ** modelUnits **   <a name="bedrock-Type-ProvisionedModelSummary-modelUnits"></a>
The number of model units allocated to the Provisioned Throughput.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: Yes

 ** provisionedModelArn **   <a name="bedrock-Type-ProvisionedModelSummary-provisionedModelArn"></a>
The Amazon Resource Name (ARN) of the Provisioned Throughput.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:provisioned-model/[a-z0-9]{12}`   
Required: Yes

 ** provisionedModelName **   <a name="bedrock-Type-ProvisionedModelSummary-provisionedModelName"></a>
The name of the Provisioned Throughput.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `([0-9a-zA-Z][_-]?)+`   
Required: Yes

 ** status **   <a name="bedrock-Type-ProvisionedModelSummary-status"></a>
The status of the Provisioned Throughput.  
Type: String  
Valid Values: `Creating | InService | Updating | Failed`   
Required: Yes

 ** commitmentDuration **   <a name="bedrock-Type-ProvisionedModelSummary-commitmentDuration"></a>
The duration for which the Provisioned Throughput was committed.  
Type: String  
Valid Values: `OneMonth | SixMonths`   
Required: No

 ** commitmentExpirationTime **   <a name="bedrock-Type-ProvisionedModelSummary-commitmentExpirationTime"></a>
The timestamp for when the commitment term of the Provisioned Throughput expires.  
Type: Timestamp  
Required: No

## See Also
<a name="API_ProvisionedModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ProvisionedModelSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ProvisionedModelSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ProvisionedModelSummary) 