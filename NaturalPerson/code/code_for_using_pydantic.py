from __future__ import annotations

from datetime import date
from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field


class Type(Enum):
    FullJsonSchemaValidator2021 = 'FullJsonSchemaValidator2021'


class CredentialSchema(BaseModel):
    id: AnyUrl = Field(
        ...,
        description='References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based',
    )
    type: Type = Field(..., description='Defines credential schema type')


class StatusPurpose(Enum):
    revocation = 'revocation'
    suspension = 'suspension'


class CredentialStatus(BaseModel):
    id: AnyUrl = Field(
        ...,
        description='References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity',
    )
    statusListCredential: Optional[AnyUrl] = Field(
        None, description='URL referencing the StatusList2021Credential'
    )
    statusListIndex: Optional[str] = Field(
        None,
        description='Integer expressed as a string. The zero based index value identifies the bit position of the status',
    )
    statusPurpose: Optional[StatusPurpose] = Field(
        None, description='Purpose of the status entry'
    )
    type: str = Field(..., description='Defines the Verifiable Credential status type')


class CredentialSubject(BaseModel):
    currentAddress: Optional[str] = Field(
        None, description='Defines the current address of the credential subject'
    )
    dateOfBirth: date = Field(
        ..., description='Defines date of birth of the credential subject'
    )
    familyName: str = Field(
        ..., description='Defines current family name(s) of the credential subject'
    )
    firstName: str = Field(
        ..., description='Defines current first name(s) of the credential subject'
    )
    gender: Optional[str] = Field(
        None, description='Defines the gender of the credential subject'
    )
    id: AnyUrl = Field(
        ...,
        description='Defines the DID of the subject that is described by the Verifiable Attestation',
    )
    nameAndFamilyNameAtBirth: Optional[str] = Field(
        None,
        description='Defines the first and the family name(s) of the credential subject at the time of their birth',
    )
    personalIdentifier: str = Field(
        ...,
        description='Defines the unique national identifier of the credential subject (constructed by the sending Member State in accordance with the technical specifications for the purposes of cross-border identification and which is as persistent as possible in time)',
    )
    placeOfBirth: Optional[str] = Field(
        None, description='Defines the place where the credential subjectis born'
    )


class EvidenceItem(BaseModel):
    documentPresence: Optional[List[str]] = None
    evidenceDocument: Optional[List[str]] = None
    id: str = Field(
        ...,
        description='If present, it MUST contain a URL that points to where more information about this instance of evidence can be found',
    )
    subjectPresence: Optional[str] = Field(
        None, description='Description to be completed'
    )
    type: List[str] = Field(..., description='Defines the evidence type')


class Proof(BaseModel):
    created: AwareDatetime = Field(
        ..., description='Defines the date and time, when the proof has been created'
    )
    jws: str = Field(..., description='Defines the proof value in JWS format')
    proofPurpose: str = Field(..., description='Defines the purpose of the proof')
    type: str = Field(..., description='Defines the proof type')
    verificationMethod: str = Field(
        ...,
        description='Contains information about the verification method / proof mechanisms',
    )


class NaturalPerson(BaseModel):
    credentialSchema: Optional[CredentialSchema] = Field(
        None,
        description='Contains information about the credential schema (template) on which the Verifiable Authorisation is based',
    )
    credentialStatus: Optional[CredentialStatus] = Field(
        None,
        description='Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)',
    )
    credentialSubject: Optional[CredentialSubject] = Field(
        None,
        description='Defines additional information about the subject that is described by the Verifiable ID',
    )
    evidence: Optional[List[EvidenceItem]] = Field(
        None,
        description='Contains information about the process which resulted in the issuance of the Verifiable Attestation',
    )
    expirationDate: Optional[AwareDatetime] = Field(
        None,
        description='Defines the date and time, when the Verifiable Attestation expires',
    )
    id: Optional[AnyUrl] = Field(
        None, description='Defines unique identifier of the Verifiable Attestation'
    )
    issuanceDate: Optional[AwareDatetime] = Field(
        None,
        description='Defines the date and time, when the Verifiable Attestation becomes valid',
    )
    issued: Optional[AwareDatetime] = Field(
        None, description='Defines when the Verifiable Attestation was issued'
    )
    issuer: Optional[AnyUrl] = Field(
        None, description='Defines the issuer of the Verifiable Attestation'
    )
    proof: Optional[Proof] = Field(
        None, description='Contains information about the proof'
    )
    type: Optional[List[str]] = Field(
        None, description='Defines the Verifiable Credential type'
    )
    validFrom: Optional[AwareDatetime] = Field(
        None,
        description='Defines the date and time, when the Verifiable Attestation becomes valid',
    )
    validUntil: Optional[AwareDatetime] = Field(
        None,
        description='Defines the date and time, when the Verifiable Attestation expires',
    )
