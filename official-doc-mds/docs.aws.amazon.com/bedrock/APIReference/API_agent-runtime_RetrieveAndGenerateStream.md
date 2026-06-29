

# RetrieveAndGenerateStream
<a name="API_agent-runtime_RetrieveAndGenerateStream"></a>

Queries a knowledge base and generates responses based on the retrieved results, with output in streaming format.

**Note**  
This API cannot be used with managed knowledge bases. Use [AgenticRetrieveStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html) or [Retrieve](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html) with managed knowledge bases.

**Note**  
The AWS CLI doesn't support streaming operations in Amazon Bedrock, including `InvokeModelWithResponseStream`.

This operation requires permission for the ` bedrock:RetrieveAndGenerate` action.

## Request Syntax
<a name="API_agent-runtime_RetrieveAndGenerateStream_RequestSyntax"></a>

```
POST /retrieveAndGenerateStream HTTP/1.1
Content-type: application/json

{
   "input": { 
      "text": "{{string}}"
   },
   "retrieveAndGenerateConfiguration": { 
      "externalSourcesConfiguration": { 
         "generationConfiguration": { 
            "additionalModelRequestFields": { 
               "{{string}}" : {{JSON value}} 
            },
            "guardrailConfiguration": { 
               "guardrailId": "{{string}}",
               "guardrailVersion": "{{string}}"
            },
            "inferenceConfig": { 
               "textInferenceConfig": { 
                  "maxTokens": {{number}},
                  "stopSequences": [ "{{string}}" ],
                  "temperature": {{number}},
                  "topP": {{number}}
               }
            },
            "performanceConfig": { 
               "latency": "{{string}}"
            },
            "promptTemplate": { 
               "textPromptTemplate": "{{string}}"
            }
         },
         "modelArn": "{{string}}",
         "sources": [ 
            { 
               "byteContent": { 
                  "contentType": "{{string}}",
                  "data": {{blob}},
                  "identifier": "{{string}}"
               },
               "s3Location": { 
                  "uri": "{{string}}"
               },
               "sourceType": "{{string}}"
            }
         ]
      },
      "knowledgeBaseConfiguration": { 
         "generationConfiguration": { 
            "additionalModelRequestFields": { 
               "{{string}}" : {{JSON value}} 
            },
            "guardrailConfiguration": { 
               "guardrailId": "{{string}}",
               "guardrailVersion": "{{string}}"
            },
            "inferenceConfig": { 
               "textInferenceConfig": { 
                  "maxTokens": {{number}},
                  "stopSequences": [ "{{string}}" ],
                  "temperature": {{number}},
                  "topP": {{number}}
               }
            },
            "performanceConfig": { 
               "latency": "{{string}}"
            },
            "promptTemplate": { 
               "textPromptTemplate": "{{string}}"
            }
         },
         "knowledgeBaseId": "{{string}}",
         "modelArn": "{{string}}",
         "orchestrationConfiguration": { 
            "additionalModelRequestFields": { 
               "{{string}}" : {{JSON value}} 
            },
            "inferenceConfig": { 
               "textInferenceConfig": { 
                  "maxTokens": {{number}},
                  "stopSequences": [ "{{string}}" ],
                  "temperature": {{number}},
                  "topP": {{number}}
               }
            },
            "performanceConfig": { 
               "latency": "{{string}}"
            },
            "promptTemplate": { 
               "textPromptTemplate": "{{string}}"
            },
            "queryTransformationConfiguration": { 
               "type": "{{string}}"
            }
         },
         "retrievalConfiguration": { 
            "managedSearchConfiguration": { 
               "filter": { ... },
               "numberOfResults": {{number}},
               "rerankingConfiguration": { 
                  "bedrockRerankingConfiguration": { 
                     "metadataConfiguration": { 
                        "selectionMode": "{{string}}",
                        "selectiveModeConfiguration": { ... }
                     },
                     "modelConfiguration": { 
                        "additionalModelRequestFields": { 
                           "{{string}}" : {{JSON value}} 
                        },
                        "modelArn": "{{string}}"
                     },
                     "numberOfRerankedResults": {{number}}
                  },
                  "type": "{{string}}"
               },
               "rerankingModelType": "{{string}}"
            },
            "vectorSearchConfiguration": { 
               "filter": { ... },
               "implicitFilterConfiguration": { 
                  "metadataAttributes": [ 
                     { 
                        "description": "{{string}}",
                        "key": "{{string}}",
                        "type": "{{string}}"
                     }
                  ],
                  "modelArn": "{{string}}"
               },
               "numberOfResults": {{number}},
               "overrideSearchType": "{{string}}",
               "rerankingConfiguration": { 
                  "bedrockRerankingConfiguration": { 
                     "metadataConfiguration": { 
                        "selectionMode": "{{string}}",
                        "selectiveModeConfiguration": { ... }
                     },
                     "modelConfiguration": { 
                        "additionalModelRequestFields": { 
                           "{{string}}" : {{JSON value}} 
                        },
                        "modelArn": "{{string}}"
                     },
                     "numberOfRerankedResults": {{number}}
                  },
                  "type": "{{string}}"
               }
            }
         }
      },
      "type": "{{string}}"
   },
   "sessionConfiguration": { 
      "kmsKeyArn": "{{string}}"
   },
   "sessionId": "{{string}}",
   "userContext": { 
      "userId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_agent-runtime_RetrieveAndGenerateStream_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent-runtime_RetrieveAndGenerateStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [input](#API_agent-runtime_RetrieveAndGenerateStream_RequestSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-request-input"></a>
Contains the query to be made to the knowledge base.  
Type: [RetrieveAndGenerateInput](API_agent-runtime_RetrieveAndGenerateInput.md) object  
Required: Yes

 ** [retrieveAndGenerateConfiguration](#API_agent-runtime_RetrieveAndGenerateStream_RequestSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-request-retrieveAndGenerateConfiguration"></a>
Contains configurations for the knowledge base query and retrieval process. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).  
Type: [RetrieveAndGenerateConfiguration](API_agent-runtime_RetrieveAndGenerateConfiguration.md) object  
Required: No

 ** [sessionConfiguration](#API_agent-runtime_RetrieveAndGenerateStream_RequestSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-request-sessionConfiguration"></a>
Contains details about the session with the knowledge base.  
Type: [RetrieveAndGenerateSessionConfiguration](API_agent-runtime_RetrieveAndGenerateSessionConfiguration.md) object  
Required: No

 ** [sessionId](#API_agent-runtime_RetrieveAndGenerateStream_RequestSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-request-sessionId"></a>
The unique identifier of the session. When you first make a `RetrieveAndGenerate` request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the `sessionId` yourself.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+`   
Required: No

 ** [userContext](#API_agent-runtime_RetrieveAndGenerateStream_RequestSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-request-userContext"></a>
Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.  
Type: [UserContext](API_agent-runtime_UserContext.md) object  
Required: No

## Response Syntax
<a name="API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amzn-bedrock-knowledge-base-session-id: {{sessionId}}
Content-type: application/json

{
   "accessDeniedException": { 
   },
   "badGatewayException": { 
   },
   "citation": { 
      "citation": { 
         "generatedResponsePart": { 
            "textResponsePart": { 
               "span": { 
                  "end": number,
                  "start": number
               },
               "text": "string"
            }
         },
         "retrievedReferences": [ 
            { 
               "content": { 
                  "audio": { 
                     "s3Uri": "string",
                     "transcription": "string"
                  },
                  "byteContent": "string",
                  "row": [ 
                     { 
                        "columnName": "string",
                        "columnValue": "string",
                        "type": "string"
                     }
                  ],
                  "text": "string",
                  "type": "string",
                  "video": { 
                     "s3Uri": "string",
                     "summary": "string"
                  }
               },
               "location": { 
                  "confluenceLocation": { 
                     "url": "string"
                  },
                  "customDocumentLocation": { 
                     "id": "string"
                  },
                  "googleDriveLocation": { 
                     "url": "string"
                  },
                  "kendraDocumentLocation": { 
                     "uri": "string"
                  },
                  "oneDriveLocation": { 
                     "url": "string"
                  },
                  "s3Location": { 
                     "uri": "string"
                  },
                  "salesforceLocation": { 
                     "url": "string"
                  },
                  "sharePointLocation": { 
                     "url": "string"
                  },
                  "sqlLocation": { 
                     "query": "string"
                  },
                  "type": "string",
                  "webLocation": { 
                     "url": "string"
                  }
               },
               "metadata": { 
                  "string" : JSON value 
               }
            }
         ]
      },
      "generatedResponsePart": { 
         "textResponsePart": { 
            "span": { 
               "end": number,
               "start": number
            },
            "text": "string"
         }
      },
      "retrievedReferences": [ 
         { 
            "content": { 
               "audio": { 
                  "s3Uri": "string",
                  "transcription": "string"
               },
               "byteContent": "string",
               "row": [ 
                  { 
                     "columnName": "string",
                     "columnValue": "string",
                     "type": "string"
                  }
               ],
               "text": "string",
               "type": "string",
               "video": { 
                  "s3Uri": "string",
                  "summary": "string"
               }
            },
            "location": { 
               "confluenceLocation": { 
                  "url": "string"
               },
               "customDocumentLocation": { 
                  "id": "string"
               },
               "googleDriveLocation": { 
                  "url": "string"
               },
               "kendraDocumentLocation": { 
                  "uri": "string"
               },
               "oneDriveLocation": { 
                  "url": "string"
               },
               "s3Location": { 
                  "uri": "string"
               },
               "salesforceLocation": { 
                  "url": "string"
               },
               "sharePointLocation": { 
                  "url": "string"
               },
               "sqlLocation": { 
                  "query": "string"
               },
               "type": "string",
               "webLocation": { 
                  "url": "string"
               }
            },
            "metadata": { 
               "string" : JSON value 
            }
         }
      ]
   },
   "conflictException": { 
   },
   "dependencyFailedException": { 
   },
   "guardrail": { 
      "action": "string"
   },
   "internalServerException": { 
   },
   "output": { 
      "text": "string"
   },
   "resourceNotFoundException": { 
   },
   "serviceQuotaExceededException": { 
   },
   "throttlingException": { 
   },
   "validationException": { 
   }
}
```

## Response Elements
<a name="API_agent-runtime_RetrieveAndGenerateStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [sessionId](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-sessionId"></a>
The session ID.  
Length Constraints: Minimum length of 2. Maximum length of 100.  
Pattern: `[0-9a-zA-Z._:-]+` 

The following data is returned in JSON format by the service.

 ** [accessDeniedException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-accessDeniedException"></a>
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 403

 ** [badGatewayException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-badGatewayException"></a>
The request failed due to a bad gateway error.  
Type: Exception  
HTTP Status Code: 502

 ** [citation](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-citation"></a>
A citation event.  
Type: [CitationEvent](API_agent-runtime_CitationEvent.md) object

 ** [conflictException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-conflictException"></a>
Error occurred because of a conflict while performing an operation.  
Type: Exception  
HTTP Status Code: 409

 ** [dependencyFailedException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-dependencyFailedException"></a>
The request failed due to a dependency error.  
Type: Exception  
HTTP Status Code: 424

 ** [guardrail](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-guardrail"></a>
A guardrail event.  
Type: [GuardrailEvent](API_agent-runtime_GuardrailEvent.md) object

 ** [internalServerException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-internalServerException"></a>
An internal server error occurred. Retry your request.  
Type: Exception  
HTTP Status Code: 500

 ** [output](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-output"></a>
An output event.  
Type: [RetrieveAndGenerateOutputEvent](API_agent-runtime_RetrieveAndGenerateOutputEvent.md) object

 ** [resourceNotFoundException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-resourceNotFoundException"></a>
The specified resource ARN was not found. For troubleshooting this error, see [ResourceNotFound](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-resource-not-found) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 404

 ** [serviceQuotaExceededException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-serviceQuotaExceededException"></a>
Your request exceeds the service quota for your account. You can view your quotas at [Viewing service quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html). You can resubmit your request later.  
Type: Exception  
HTTP Status Code: 400

 ** [throttlingException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-throttlingException"></a>
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 429

 ** [validationException](#API_agent-runtime_RetrieveAndGenerateStream_ResponseSyntax) **   <a name="bedrock-agent-runtime_RetrieveAndGenerateStream-response-validationException"></a>
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide.  
Type: Exception  
HTTP Status Code: 400

## Errors
<a name="API_agent-runtime_RetrieveAndGenerateStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions. Check your permissions and retry your request.  
HTTP Status Code: 403

 ** BadGatewayException **   
There was an issue with a dependency due to a server issue. Retry your request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 502

 ** ConflictException **   
There was a conflict performing an operation. Resolve the conflict and retry your request.  
HTTP Status Code: 409

 ** DependencyFailedException **   
There was an issue with a dependency. Check the resource configurations and retry the request.    
 ** resourceName **   
The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or AWS STS.
HTTP Status Code: 424

 ** InternalServerException **   
An internal server error occurred. Retry your request.    
 ** reason **   
The reason for the exception. If the reason is `BEDROCK_MODEL_INVOCATION_SERVICE_UNAVAILABLE`, the model invocation service is unavailable. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 400

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_agent-runtime_RetrieveAndGenerateStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/RetrieveAndGenerateStream) 