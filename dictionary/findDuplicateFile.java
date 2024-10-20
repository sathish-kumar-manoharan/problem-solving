/*
 * https://leetcode.com/problems/find-duplicate-file-in-system/
 * Time complexity : O(n∗x). where n strings of average length , x is parsed.
 * Space complexity : O(n∗x). map and res size grows upto n∗x.
 * 
 * 
Follow up:

*Imagine you are given a real file system, how will you search files? DFS or BFS?
*If the file content is very large (GB level), how will you modify your solution?
*If you can only read the file by 1kb each time, how will you modify your solution?
*What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
*How to make sure the duplicated files you find are not false positive?

Searching Files: DFS vs. BFS
When searching files in a real file system, both Depth-First Search (DFS) and Breadth-First Search (BFS) have their pros and cons.

DFS: This approach is memory efficient as it only needs to store the current path from the root to the leaf node. It is suitable for deep file systems where files are nested within many directories. However, it might not be the best choice if you need to find the shortest path to a file.
BFS: This approach is better for finding the shortest path to a file because it explores all nodes at the present depth level before moving on to nodes at the next depth level. However, it requires more memory as it needs to store all nodes at the current depth level.
Given these points, DFS is generally preferred for file system searches due to its lower memory usage12.

Handling Large File Content (GB Level)
For very large files, reading the entire file into memory is impractical. Instead, you can use a streaming approach to process the file in chunks. Here's how you can modify your solution:

import java.io.*;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;

public class Solution {
    private static MessageDigest messageDigest;

    static {
        try {
            messageDigest = MessageDigest.getInstance("SHA-512");
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Cannot initialize SHA-512 hash function", e);
        }
    }

    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> contentMap = new HashMap<>();

        for (String pathInfo : paths) {
            String[] parts = pathInfo.split(" ");
            String directory = parts;

            for (int i = 1; i < parts.length; i++) {
                String fileInfo = parts[i];
                int openParenthesisIndex = fileInfo.indexOf('(');
                String fileName = fileInfo.substring(0, openParenthesisIndex);
                String fileContent = fileInfo.substring(openParenthesisIndex + 1, fileInfo.length() - 1);

                String fullPath = directory + "/" + fileName;

                try (InputStream fileInput = new FileInputStream(fullPath)) {
                    byte[] buffer = new byte;
                    int bytesRead;
                    while ((bytesRead = fileInput.read(buffer)) != -1) {
                        messageDigest.update(buffer, 0, bytesRead);
                    }
                    String uniqueFileHash = new BigInteger(1, messageDigest.digest()).toString(16);

                    contentMap.putIfAbsent(uniqueFileHash, new ArrayList<>());
                    contentMap.get(uniqueFileHash).add(fullPath);
                } catch (IOException e) {
                    throw new RuntimeException("Cannot read file " + fullPath, e);
                }
            }
        }

        List<List<String>> duplicates = new ArrayList<>();
        for (List<String> group : contentMap.values()) {
            if (group.size() > 1) {
                duplicates.add(group);
            }
        }

        return duplicates;
    }
}
Reading File by 1KB Each Time
If you can only read the file by 1KB each time, you can use a similar approach as above, but ensure that you read the file in 1KB chunks:

try (InputStream fileInput = new FileInputStream(fullPath)) {
    byte[] buffer = new byte;
    int bytesRead;
    while ((bytesRead = fileInput.read(buffer)) != -1) {
        messageDigest.update(buffer, 0, bytesRead);
    }
    String uniqueFileHash = new BigInteger(1, messageDigest.digest()).toString(16);
    // Continue with the rest of the logic
}
Time Complexity
The time complexity of the modified solution is O(n * m), where n is the number of files and m is the size of the largest file. The most time-consuming part is reading the file content and computing the hash. The most memory-consuming part is storing the hash values and file paths.

Optimizing
To optimize, you can:

Use a more efficient hashing algorithm if SHA-512 is too slow.
Parallelize the file reading and hashing process to utilize multiple CPU cores.
Use memory-mapped files to speed up file reading.
Ensuring No False Positives
To ensure that the duplicated files you find are not false positives:

Use a strong cryptographic hash function like SHA-512 to minimize hash collisions.
Compare the file sizes before comparing the hashes.
If two files have the same hash, you can do a byte-by-byte comparison to confirm they are identical.
 */
class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> contentMap = new HashMap<>();

        for (String pathInfo : paths) {
            String[] parts = pathInfo.split(" ");
            String directory = parts[0];

            for (int i = 1; i < parts.length; i++) {
                String fileInfo = parts[i];
                int openParenthesisIndex = fileInfo.indexOf('(');
                String fileName = fileInfo.substring(0, openParenthesisIndex);
                String fileContent = fileInfo.substring(openParenthesisIndex + 1, fileInfo.length() - 1);

                String fullPath = directory + "/" + fileName;

                contentMap.putIfAbsent(fileContent, new ArrayList<>());
                contentMap.get(fileContent).add(fullPath);
            }
        }

        List<List<String>> duplicates = new ArrayList<>();
        for (List<String> group : contentMap.values()) {
            if (group.size() > 1) {
                duplicates.add(group);
            }
        }

        return duplicates;
    }
}