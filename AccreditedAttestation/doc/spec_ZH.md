<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。认可测试  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/AccreditedAttestation/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**EBSI认可的可验证证明的格式**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `credentialSchema[object]`: 包含可验证授权所依据的凭证模式（模板）的信息。  - `credentialStatus[object]`: 包含关于如何验证可核查证明的状态的信息（通过撤销和认可登记处，RER）。  - `credentialSubject[object]`: 定义了可验证的证明所描述的主体的信息  - `evidence[array]`: 包含有关导致签发可核查证明的过程的信息  - `expirationDate[string]`: 定义了可验证证明到期的日期和时间。  - `id[string]`: 定义了可验证证明的唯一标识符  - `issuanceDate[string]`: 定义日期和时间，当可验证的证明变得有效时。  - `issued[string]`: 定义了可验证证明的签发时间  - `issuer[string]`: 定义了可验证证明的签发者  - `proof[object]`: 包含有关证明的信息  - `termsOfUse[array]`: 包含签发经认可的可核查证明的条款  - `type[array]`: 定义了可验证凭证的类型  - `validFrom[string]`: 定义日期和时间，当可验证的证明变得有效时。  - `validUntil[string]`: 定义了可验证证明到期的日期和时间。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
源自EBSI json模式的数据模型https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas。@context属性已从定义中删除，因为它在NGSI-LD中是强制性的，不需要明确记录。只有在关键值链接数据中才有这个例子  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
AccreditedAttestation:    
  description: Schema of an EBSI Accredited Verifiable Attestation    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: Property. References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
        type:    
          description: Property. Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialStatus:    
      description: 'Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)'    
      properties:    
        id:    
          description: Property. References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
        statusListCredential:    
          description: Property. URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
        statusListIndex:    
          description: Property. Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
        statusPurpose:    
          description: Property. Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
        type:    
          description: Property. Defines the Verifiable Credential status type    
          type: string    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialSubject:    
      description: Defines information about the subject that is described by the Verifiable Attestation    
      properties:    
        id:    
          description: Property. Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          documentPresence:    
            items:    
              description: Property. Description to be completed    
              type: string    
            type: array    
          evidenceDocument:    
            items:    
              description: Property. Description to be completed    
              type: string    
            type: array    
          id:    
            description: 'Property. If present, it MUST contain a URL that points to where more information about this instance of evidence can be found.'    
            type: string    
          subjectPresence:    
            description: Property. Description to be completed    
            type: string    
          type:    
            description: Property. Defines the evidence type    
            items:    
              type: string    
            type: array    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expirationDate:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Defines unique identifier of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    issuanceDate:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issued:    
      description: Defines when the Verifiable Attestation was issued    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issuer:    
      description: Defines the issuer of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        created:    
          description: 'Property. Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
        jws:    
          description: Property. Defines the proof value in JWS format    
          type: string    
        proofPurpose:    
          description: Property. Defines the purpose of the proof    
          type: string    
        type:    
          description: Property. Defines the proof type    
          type: string    
        verificationMethod:    
          description: Property. Contains information about the verification method / proof mechanisms    
          type: string    
      required:    
        - type    
        - proofPurpose    
        - created    
        - verificationMethod    
        - jws    
      type: object    
      x-ngsi:    
        type: Property    
    termsOfUse:    
      description: Contains the terms under which the Accredited Verifiable Attestation was issued    
      items:    
        description: Property. Description to be completed    
        properties:    
          id:    
            description: Property. Contains a URL that points to where more information about this instance of terms of use can be found.    
            format: uri    
            type: string    
          type:    
            description: Property. Defines the type of terms of use.    
            type: string    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: Defines the Verifiable Credential type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validUntil:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-accredited-attestation/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/AccreditedAttestation/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
不可用JSON-LD格式的AccreditedAttestation的例子作为key-values。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
不提供JSON-LD格式的AccreditedAttestation规范化的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
#### AccreditedAttestation NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的AccreditedAttestation的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:uuid:58afcb57-81f9-4e8c-817b-01f0597d6801",  
  "type": [  
    "VerifiableCredential",  
    "VerifiableAttestation",  
    "AccreditedVerifiableAttestation"  
  ],  
  "issuer": "did:ebsi:00001234",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "expirationDate": "2024-06-22T14:11:44Z",  
  "issued": "2020-06-22T14:11:44Z",  
  "termsOfUse": [  
    {  
      "id": "https://essif.europa.eu/accreditation/45",  
      "type": "VerifiableAccreditation"  
    }  
  ],  
  "credentialSubject": {  
    "id": "did:ebsi:00001235"  
  },  
  "credentialStatus": {  
    "id": "https://essif.europa.eu/status/45",  
    "type": "CredentialsStatusList2020"  
  },  
  "credentialSchema": {  
    "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0x4a131e78474b35ca4c93d4904cae9f2013cd53794ce521f6fcfac17ac460c6e5",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
不提供JSON-LD格式的AccreditedAttestation规范化的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
