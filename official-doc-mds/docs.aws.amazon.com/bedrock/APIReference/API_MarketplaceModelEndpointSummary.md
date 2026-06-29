

# MarketplaceModelEndpointSummary
<a name="API_MarketplaceModelEndpointSummary"></a>

Provides a summary of an endpoint for a model from Amazon Bedrock Marketplace.

## Contents
<a name="API_MarketplaceModelEndpointSummary_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-MarketplaceModelEndpointSummary-createdAt"></a>
The timestamp when the endpoint was created.  
Type: Timestamp  
Required: Yes

 ** endpointArn **   <a name="bedrock-Type-MarketplaceModelEndpointSummary-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** modelSourceIdentifier **   <a name="bedrock-Type-MarketplaceModelEndpointSummary-modelSourceIdentifier"></a>
The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*arn:aws:sagemaker:.*:hub-content/SageMakerPublicHub/Model/.*`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-MarketplaceModelEndpointSummary-updatedAt"></a>
The timestamp when the endpoint was last updated.  
Type: Timestamp  
Required: Yes

 ** status **   <a name="bedrock-Type-MarketplaceModelEndpointSummary-status"></a>
The overall status of the endpoint in Amazon Bedrock Marketplace.  
Type: String  
Valid Values: `REGISTERED | INCOMPATIBLE_ENDPOINT`   
Required: No

 ** statusMessage **   <a name="bedrock-Type-MarketplaceModelEndpointSummary-statusMessage"></a>
Additional information about the overall status, if available.  
Type: String  
Required: No

## See Also
<a name="API_MarketplaceModelEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/MarketplaceModelEndpointSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/MarketplaceModelEndpointSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/MarketplaceModelEndpointSummary) 