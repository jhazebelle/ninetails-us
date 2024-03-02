// Here are the requirements for Task 2 in the Wells Fargo SWE Program:
// Create a class for each entity in your data model (these should be placed in the entities directory). Respect the following when implementing your data model:
// Each entity must be annotated with the @Entity type, which can be found in the javax.persistence package.
// Each id must be auto-generated.
// Each instance variable must contain either a column or a relationship annotation.
// Each class must contain a constructor which initializes all instance variables.
// Each class must expose a getter and setter for each instance variable (no setter for the id field is required).
// Lean on the existing entities (one has been provided for you) for hints on how to accomplish the above.

// I was given the advisor class file when I cloned the project. See below for code to use as a hint for the other entities.

package com.wellsfargo.counselor.entity;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Advisor {

    @Id
    @GeneratedValue()
    private long advisorId;

    @Column(nullable = false)
    private String firstName;

    @Column(nullable = false)
    private String lastName;

    @Column(nullable = false)
    private String address;

    @Column(nullable = false)
    private String phone;

    @Column(nullable = false)
    private String email;

    protected Advisor() {

    }

    public Advisor(String firstName, String lastName, String address, String phone, String email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.address = address;
        this.phone = phone;
        this.email = email;
    }

    public Long getAdvisorId() {
        return advisorId;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
