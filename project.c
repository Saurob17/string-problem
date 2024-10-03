#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_C 11  // Maximum number of candidates

// Define the structure for a Candidate
typedef struct Candidate {
    char name[50];  // Candidate name
    int votes;      // Number of votes received
} Candidate;

// Global array to hold all candidates
Candidate allCandidates[MAX_C];
int candidateCount = 0;  // Number of candidates participating

// Function declarations
void fillCandidate(int cNum);

void displayAllCandidates();

void getVotes(int voterCount);

void getResults();

int getValidIntegerInput(const char *prompt, int minValue, int maxValue);

// Main function: Entry point of the program
int main() {

    // Get the number of candidates with validation
    candidateCount = getValidIntegerInput("Enter the number of candidates (1-10): ", 1, MAX_C - 1);

    // Fill the candidate details
    for (int i = 0; i < candidateCount; i++) {
        fillCandidate(i);  // Get candidate information
    }

    // Get the number of voters with validation
    int numVoters = getValidIntegerInput("Enter the number of voters: ", 1, 10000);  // Assuming a large upper limit for voters
    
    // Clear the terminal screen
    system("clear");  // Use "clear" for Linux

    // Start the voting process
    for (int i = 0; i < numVoters; i++) {

        getVotes(i);  // Get the vote from each voter
    }

    // Display the results of the voting
    getResults();

    return 0;
}

// Function to input candidate information
void fillCandidate(int cNum) {

    // Get candidate name from the user
    printf("Enter the name of candidate %d: ", cNum + 1);
    scanf("%s", allCandidates[cNum].name);

    // Initialize the vote count to 0
    allCandidates[cNum].votes = 0;
}

// Function to display the list of all candidates
void displayAllCandidates() {

    if (candidateCount <= 0) {

        // Error if the candidate array is empty
        perror("Invalid Candidate Array\n");

        return;
    }

    // Display each candidate's number, name
    for (int j = 0; j < candidateCount; j++) {

        printf("%d. %s\n", j + 1, allCandidates[j].name);

    }
}

// Function to handle voting for each voter
void getVotes(int voterCount) {
    int choice;

    while (1) {

        // Display all candidates with numbers
        displayAllCandidates();

        // Print the actual candidate count in the prompt
        printf("Voter %d, please enter your choice (1-%d): ", voterCount + 1, candidateCount);

        // Use the input validation function to get the voter's choice
        choice = getValidIntegerInput("", 1, candidateCount);

        // If the choice is valid, break the loop and count the vote
        if (choice >= 1 && choice <= candidateCount) {

            allCandidates[choice - 1].votes++;  // Register the vote
            break;  // Valid vote, exit the loop

        } 
        
        else {

            // Invalid choice, prompt again
            printf("Invalid choice! Please enter a valid candidate number between 1 and %d.\n", candidateCount);
        }
    }

    // Clear the screen after each vote (for better display)
    system("clear");  // Use "clear" instead of "cls" for Linux
}

// Function to display the results of the voting
void getResults() {

    int maxVotes = 0;  // Track the maximum votes received
    int winnerIndex = -1;  // Index of the candidate with max votes
    int winnerFrequency = 0;  // Track how many candidates got the maximum votes

    // Display the votes received by each candidate
    printf("\n-----VOTES PER CANDIDATE-----\n");
    
    for (int i = 0; i < candidateCount; i++) {

        printf("%d.%s received %d votes\n", i + 1, allCandidates[i].name, allCandidates[i].votes);

        // Update the maximum votes and winner
        if (allCandidates[i].votes > maxVotes) {
            maxVotes = allCandidates[i].votes;
            winnerIndex = i;
        }
    }

    // Check if there's a tie (multiple candidates with the same max votes)
    for (int i = 0; i < candidateCount; i++) {

        if (allCandidates[i].votes == maxVotes) {
            winnerFrequency++;
        }

    }

    // Display the final result
    printf("\n-----RESULT-----\n");

    if (winnerFrequency > 1) {

        printf("It's a tie! No candidate has a majority.\n");
    } else if (winnerIndex != -1) {

        printf("The winner is candidate number(%d):%s\nwith %d votes!\n", winnerIndex + 1, allCandidates[winnerIndex].name, maxVotes);
    } 
    
    else {
        printf("No winner\n");
    }
}

// Function to get a valid integer input with range validation
int getValidIntegerInput(const char *prompt, int minValue, int maxValue) {
    int input;
    char ch;

    // Continue prompting until valid input is received
    while (1) {

        printf("%s", prompt);

        if (scanf("%d", &input) != 1) {

            // Invalid input (not a number)
            while ((ch = getchar()) != '\n' && ch != EOF);  // Clear invalid input from buffer
            printf("Invalid input. Please enter a valid number.\n");
        } 
        
        else if (input < minValue || input > maxValue) {

            // Valid number but out of range
            printf("Input out of range. Please enter a number between %d and %d.\n", minValue, maxValue);

        } 
        else {

            return input;  // Valid input within range
        }
    }
}
