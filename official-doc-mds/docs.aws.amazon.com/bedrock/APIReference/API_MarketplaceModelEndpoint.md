

# MarketplaceModelEndpoint
<a name="API_MarketplaceModelEndpoint"></a>

Contains details about an endpoint for a model from Amazon Bedrock Marketplace.

## Contents
<a name="API_MarketplaceModelEndpoint_Contents"></a>

 ** createdAt **   <a name="bedrock-Type-MarketplaceModelEndpoint-createdAt"></a>
The timestamp when the endpoint was registered.  
Type: Timestamp  
Required: Yes

 ** endpointArn **   <a name="bedrock-Type-MarketplaceModelEndpoint-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Required: Yes

 ** endpointConfig **   <a name="bedrock-Type-MarketplaceModelEndpoint-endpointConfig"></a>
The configuration of the endpoint, including the number and type of instances used.  
Type: [EndpointConfig](API_EndpointConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** endpointStatus **   <a name="bedrock-Type-MarketplaceModelEndpoint-endpointStatus"></a>
The current status of the endpoint (e.g., Creating, InService, Updating, Failed).  
Type: String  
Required: Yes

 ** modelSourceIdentifier **   <a name="bedrock-Type-MarketplaceModelEndpoint-modelSourceIdentifier"></a>
The ARN of the model from Amazon Bedrock Marketplace that is deployed on this endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `.*arn:aws:sagemaker:.*:hub-content/SageMakerPublicHub/Model/.*`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-MarketplaceModelEndpoint-updatedAt"></a>
The timestamp when the endpoint was last updated.  
Type: Timestamp  
Required: Yes

 ** endpointStatusMessage **   <a name="bedrock-Type-MarketplaceModelEndpoint-endpointStatusMessage"></a>
Additional information about the endpoint status, if available.  
Type: String  
Required: No

 ** status **   <a name="bedrock-Type-MarketplaceModelEndpoint-status"></a>
The overall status of the endpoint in Amazon Bedrock Marketplace (e.g., ACTIVE, INACTIVE).  
Type: String  
Valid Values: `REGISTERED | INCOMPATIBLE_ENDPOINT`   
Required: No

 ** statusMessage **   <a name="bedrock-Type-MarketplaceModelEndpoint-statusMessage"></a>
Additional information about the overall status, if available.  
Type: String  
Required: No

## See Also
<a name="API_MarketplaceModelEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/MarketplaceModelEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/MarketplaceModelEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/MarketplaceModelEndpoint) 