

# CreateGateway
<a name="API_CreateGateway"></a>

Creates a gateway for Amazon Bedrock Agent. A gateway serves as an integration point between your agent and external services.

If you specify `CUSTOM_JWT` as the `authorizerType`, you must provide an `authorizerConfiguration`.

## Request Syntax
<a name="API_CreateGateway_RequestSyntax"></a>

```
POST /gateways/ HTTP/1.1
Content-type: application/json

{
   "authorizerConfiguration": { ... },
   "authorizerType": "{{string}}",
   "clientToken": "{{string}}",
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
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateGateway_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authorizerConfiguration](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-authorizerConfiguration"></a>
The authorizer configuration for the gateway. Required if `authorizerType` is `CUSTOM_JWT`.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [authorizerType](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-authorizerType"></a>
The type of authorizer to use for the gateway.  
+  `CUSTOM_JWT` - Authorize with a bearer token.
+  `AWS_IAM` - Authorize with your AWS IAM credentials.
+  `NONE` - No authorization
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM | NONE | AUTHENTICATE_ONLY`   
Required: Yes

 ** [clientToken](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-description"></a>
The description of the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [exceptionLevel](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-exceptionLevel"></a>
The level of detail in error messages returned when invoking the gateway.  
+ If the value is `DEBUG`, granular exception messages are returned to help a user debug the gateway.
+ If the value is omitted, a generic error message is returned to the end user.
Type: String  
Valid Values: `DEBUG`   
Required: No

 ** [interceptorConfigurations](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-interceptorConfigurations"></a>
A list of configuration settings for a gateway interceptor. Gateway interceptors allow custom code to be invoked during gateway invocations.  
Type: Array of [GatewayInterceptorConfiguration](API_GatewayInterceptorConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: No

 ** [kmsKeyArn](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt data associated with the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [name](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-name"></a>
The name of the gateway. The name must be unique within your account.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,48}`   
Required: Yes

 ** [policyEngineConfiguration](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-policyEngineConfiguration"></a>
The policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.  
Type: [GatewayPolicyEngineConfiguration](API_GatewayPolicyEngineConfiguration.md) object  
Required: No

 ** [protocolConfiguration](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-protocolConfiguration"></a>
The configuration settings for the protocol specified in the `protocolType` parameter.  
Type: [GatewayProtocolConfiguration](API_GatewayProtocolConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** [protocolType](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-protocolType"></a>
The protocol type for the gateway.  
Type: String  
Valid Values: `MCP`   
Required: No

 ** [roleArn](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that provides permissions for the gateway to access AWS services.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

 ** [tags](#API_CreateGateway_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-request-tags"></a>
A map of key-value pairs to associate with the gateway as metadata tags.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateGateway_ResponseSyntax"></a>

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
<a name="API_CreateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [authorizerConfiguration](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-authorizerConfiguration"></a>
The authorizer configuration for the created gateway.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [authorizerType](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-authorizerType"></a>
The type of authorizer used by the gateway.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM | NONE | AUTHENTICATE_ONLY` 

 ** [createdAt](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-createdAt"></a>
The timestamp when the gateway was created.  
Type: Timestamp

 ** [customTransformConfiguration](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-customTransformConfiguration"></a>
The custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.  
Type: [CustomTransformConfiguration](API_CustomTransformConfiguration.md) object

 ** [description](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-description"></a>
The description of the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [exceptionLevel](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-exceptionLevel"></a>
The level of detail in error messages returned when invoking the gateway.  
+ If the value is `DEBUG`, granular exception messages are returned to help a user debug the gateway.
+ If the value is omitted, a generic error message is returned to the end user.
Type: String  
Valid Values: `DEBUG` 

 ** [gatewayArn](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-gatewayArn"></a>
The Amazon Resource Name (ARN) of the created gateway.  
Type: String  
Pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}` 

 ** [gatewayId](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-gatewayId"></a>
The unique identifier of the created gateway.  
Type: String  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}` 

 ** [gatewayUrl](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-gatewayUrl"></a>
The URL endpoint for the created gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [interceptorConfigurations](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-interceptorConfigurations"></a>
The list of interceptor configurations for the created gateway.  
Type: Array of [GatewayInterceptorConfiguration](API_GatewayInterceptorConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.

 ** [kmsKeyArn](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt data associated with the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [name](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-name"></a>
The name of the gateway.  
Type: String  
Pattern: `([0-9a-zA-Z][-]?){1,48}` 

 ** [policyEngineConfiguration](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-policyEngineConfiguration"></a>
The policy engine configuration for the created gateway.  
Type: [GatewayPolicyEngineConfiguration](API_GatewayPolicyEngineConfiguration.md) object

 ** [protocolConfiguration](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-protocolConfiguration"></a>
The configuration settings for the protocol used by the gateway.  
Type: [GatewayProtocolConfiguration](API_GatewayProtocolConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [protocolType](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-protocolType"></a>
The protocol type of the gateway.  
Type: String  
Valid Values: `MCP` 

 ** [roleArn](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+` 

 ** [status](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-status"></a>
The current status of the gateway.  
Type: String  
Valid Values: `CREATING | UPDATING | UPDATE_UNSUCCESSFUL | DELETING | READY | FAILED` 

 ** [statusReasons](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-statusReasons"></a>
The reasons for the current status of the gateway.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Length Constraints: Minimum length of 0. Maximum length of 2048.

 ** [updatedAt](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-updatedAt"></a>
The timestamp when the gateway was last updated.  
Type: Timestamp

 ** [wafConfiguration](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-wafConfiguration"></a>
The AWS WAF configuration for the gateway.  
Type: [WafConfiguration](API_WafConfiguration.md) object

 ** [webAclArn](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-webAclArn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web ACL associated with the gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:[a-z0-9\-]+:wafv2:[a-z0-9\-]+:[0-9]{12}:regional/webacl/.+` 

 ** [workloadIdentityDetails](#API_CreateGateway_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateGateway-response-workloadIdentityDetails"></a>
The workload identity details for the created gateway.  
Type: [WorkloadIdentityDetails](API_WorkloadIdentityDetails.md) object

## Errors
<a name="API_CreateGateway_Errors"></a>

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
<a name="API_CreateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateGateway) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateGateway) 