

# UpdateGateway
<a name="API_UpdateGateway"></a>

Updates an existing gateway.

## Request Syntax
<a name="API_UpdateGateway_RequestSyntax"></a>

```
PUT /gateways/{{gatewayIdentifier}}/ HTTP/1.1
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "{{string}}",
   "customTransformConfiguration": { 
      "lambda": { 
         "arn": "{{string}}"
      }
   },
   "description": "{{string}}",
   "exceptionLevel": "{{string}}",
   "interceptorConfigurations": [ 
      { 
         "inputConfiguration": { 
            "passRequestHeaders": {{boolean}},
            "payloadFilter": { 
               "exclude": [ 
                  { ... }
               ]
            }
         },
         "interceptionPoints": [ "{{string}}" ],
         "interceptor": { ... }
      }
   ],
   "kmsKeyArn": "{{string}}",
   "name": "{{string}}",
   "policyEngineConfiguration": { 
      "arn": "{{string}}",
      "mode": "{{string}}"
   },
   "protocolConfiguration": { ... },
   "protocolType": "{{string}}",
   "roleArn": "{{string}}",
   "wafConfiguration": { 
      "failureMode": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-uri-gatewayIdentifier"></a>
The identifier of the gateway to update.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerConfiguration](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-authorizerConfiguration"></a>
The updated authorizer configuration for the gateway.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [authorizerType](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-authorizerType"></a>
The updated authorizer type for the gateway.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM | NONE | AUTHENTICATE_ONLY`   
Required: Yes

 ** [customTransformConfiguration](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-customTransformConfiguration"></a>
The updated custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.  
Type: [CustomTransformConfiguration](API_CustomTransformConfiguration.md) object  
Required: No

 ** [description](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-description"></a>
The updated description for the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [exceptionLevel](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-exceptionLevel"></a>
The level of detail in error messages returned when invoking the gateway.  
+ If the value is `DEBUG`, granular exception messages are returned to help a user debug the gateway.
+ If the value is omitted, a generic error message is returned to the end user.
Type: String  
Valid Values: `DEBUG`   
Required: No

 ** [interceptorConfigurations](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-interceptorConfigurations"></a>
The updated interceptor configurations for the gateway.  
Type: Array of [GatewayInterceptorConfiguration](API_GatewayInterceptorConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: No

 ** [kmsKeyArn](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-kmsKeyArn"></a>
The updated ARN of the AWS KMS key used to encrypt the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [name](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-name"></a>
The name of the gateway. This name must be the same as the one when the gateway was created.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,48}`   
Required: Yes

 ** [policyEngineConfiguration](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-policyEngineConfiguration"></a>
The updated policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.  
Type: [GatewayPolicyEngineConfiguration](API_GatewayPolicyEngineConfiguration.md) object  
Required: No

 ** [protocolConfiguration](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-protocolConfiguration"></a>
The configuration for a gateway protocol. This structure defines how the gateway communicates with external services.  
Type: [GatewayProtocolConfiguration](API_GatewayProtocolConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [protocolType](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-protocolType"></a>
The updated protocol type for the gateway.  
Type: String  
Valid Values: `MCP`   
Required: No

 ** [roleArn](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-roleArn"></a>
The updated IAM role ARN that provides permissions for the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [wafConfiguration](#API_UpdateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-request-wafConfiguration"></a>
The updated AWS WAF configuration for the gateway.  
Type: [WafConfiguration](API_WafConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_UpdateGateway_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "string",
   "createdAt": "string",
   "customTransformConfiguration": { 
      "lambda": { 
         "arn": "string"
      }
   },
   "description": "string",
   "exceptionLevel": "string",
   "gatewayArn": "string",
   "gatewayId": "string",
   "gatewayUrl": "string",
   "interceptorConfigurations": [ 
      { 
         "inputConfiguration": { 
            "passRequestHeaders": boolean,
            "payloadFilter": { 
               "exclude": [ 
                  { ... }
               ]
            }
         },
         "interceptionPoints": [ "string" ],
         "interceptor": { ... }
      }
   ],
   "kmsKeyArn": "string",
   "name": "string",
   "policyEngineConfiguration": { 
      "arn": "string",
      "mode": "string"
   },
   "protocolConfiguration": { ... },
   "protocolType": "string",
   "roleArn": "string",
   "status": "string",
   "statusReasons": [ "string" ],
   "updatedAt": "string",
   "wafConfiguration": { 
      "failureMode": "string"
   },
   "webAclArn": "string",
   "workloadIdentityDetails": { 
      "workloadIdentityArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authorizerConfiguration](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-authorizerConfiguration"></a>
The updated authorizer configuration for the gateway.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [authorizerType](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-authorizerType"></a>
The updated authorizer type for the gateway.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM | NONE | AUTHENTICATE_ONLY` 

 ** [createdAt](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-createdAt"></a>
The timestamp when the gateway was created.  
Type: Timestamp

 ** [customTransformConfiguration](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-customTransformConfiguration"></a>
The custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.  
Type: [CustomTransformConfiguration](API_CustomTransformConfiguration.md) object

 ** [description](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-description"></a>
The updated description of the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [exceptionLevel](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-exceptionLevel"></a>
The level of detail in error messages returned when invoking the gateway.  
+ If the value is `DEBUG`, granular exception messages are returned to help a user debug the gateway.
+ If the value is omitted, a generic error message is returned to the end user.
Type: String  
Valid Values: `DEBUG` 

 ** [gatewayArn](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the updated gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [gatewayId](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-gatewayId"></a>
The unique identifier of the updated gateway.  
Type: String  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [gatewayUrl](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-gatewayUrl"></a>
An endpoint for invoking the updated gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [interceptorConfigurations](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-interceptorConfigurations"></a>
The updated interceptor configurations for the gateway.  
Type: Array of [GatewayInterceptorConfiguration](API_GatewayInterceptorConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [kmsKeyArn](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-kmsKeyArn"></a>
The updated ARN of the KMS key used to encrypt the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-name"></a>
The name of the gateway.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,48}` 

 ** [policyEngineConfiguration](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-policyEngineConfiguration"></a>
The updated policy engine configuration for the gateway.  
Type: [GatewayPolicyEngineConfiguration](API_GatewayPolicyEngineConfiguration.md) object

 ** [protocolConfiguration](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-protocolConfiguration"></a>
The configuration for a gateway protocol. This structure defines how the gateway communicates with external services.  
Type: [GatewayProtocolConfiguration](API_GatewayProtocolConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [protocolType](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-protocolType"></a>
The updated protocol type for the gateway.  
Type: String  
Valid Values: `MCP` 

 ** [roleArn](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-roleArn"></a>
The updated IAM role ARN that provides permissions for the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-status"></a>
The current status of the updated gateway.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED` 

 ** [statusReasons](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-statusReasons"></a>
The reasons for the current status of the updated gateway.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [updatedAt](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-updatedAt"></a>
The timestamp when the gateway was last updated.  
Type: Timestamp

 ** [wafConfiguration](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-wafConfiguration"></a>
The AWS WAF configuration for the gateway.  
Type: [WafConfiguration](API_WafConfiguration.md) object

 ** [webAclArn](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-webAclArn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web ACL associated with the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:[a-z0-9\-]+:wafv2:[a-z0-9\-]+:[0-9]{12}:regional/webacl/.+` 

 ** [workloadIdentityDetails](#API_UpdateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateGateway-response-workloadIdentityDetails"></a>
The workload identity details for the updated gateway.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_UpdateGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateGateway) 