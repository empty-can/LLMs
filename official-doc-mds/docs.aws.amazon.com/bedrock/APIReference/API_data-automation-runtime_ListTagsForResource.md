

# ListTagsForResource
<a name="API_data-automation-runtime_ListTagsForResource"></a>

Lists a resources tags.

## Request Syntax
<a name="API_data-automation-runtime_ListTagsForResource_RequestSyntax"></a>

```
{
   "resourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_data-automation-runtime_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceARN](#API_data-automation-runtime_ListTagsForResource_RequestSyntax) **   <a name="bedrock-data-automation-runtime_ListTagsForResource-request-resourceARN"></a>
The ARN of the resource you want to check the tags of  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-invocation/[a-zA-Z0-9-_]+`   
Required: Yes

## Response Syntax
<a name="API_data-automation-runtime_ListTagsForResource_ResponseSyntax"></a>

```
{
   "tags": [ 
      { 
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_data-automation-runtime_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_data-automation-runtime_ListTagsForResource_ResponseSyntax) **   <a name="bedrock-data-automation-runtime_ListTagsForResource-response-tags"></a>
The requested resource's tags.  
Type: Array of [Tag](API_data-automation-runtime_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_data-automation-runtime_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 400

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 400

 ** ThrottlingException **   
  
HTTP Status Code: 400

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation-runtime_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/ListTagsForResource) 